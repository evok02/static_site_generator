from textnode import TextNode, TextType
from markdown_to_html import markdown_to_html_node
import os
import sys

def extract_title(markdown):
    title_line = ""
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            title_line = line
            break
    if not title_line:
        raise Exception("There is not title in this file... ")
    return title_line[1:].strip()

def create_path(path, folder):
    if not os.path.exists(path):
        items = path.split("/")
        create_path("/".joint(items[:-1]), items[-1])
    else:
        os.mkdir(os.path.join(path, folder))

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generatig page from {from_path} to {dest_path} using {template_path}")
    cwd = os.getcwd()
    with open(os.path.join(cwd, from_path)) as md:
        markdown_content = md.read() 
    with open(os.path.join(cwd, template_path)) as tmp:
        template_content = tmp.read() 
    body = markdown_to_html_node(markdown_content)
    title = extract_title(markdown_content)
    template_content = (template_content
                        .replace("{{ Title }}", title)
                        .replace("{{ Content }}", body)
                        .replace("href=\"/", f"href=\"{basepath}/")
                        .replace("src=\"/", f"src=\"{basepath}/")
                        )

    print(template_content)
    with open(os.path.join(cwd, dest_path), "w") as f:
        f.write(template_content)


def generate_page_recursively(source, template_path, destination, basepath):
    if not os.path.exists(source):
        raise Exception("Path doesn't exist...")
    for item in os.listdir(source):
        current_path = os.path.join(source, item)
        if os.path.isdir(current_path):
            new_destination = os.path.join(destination, item)
            print(f"Creating new directory in: {current_path}")
            os.mkdir(new_destination)
            generate_page_recursively(current_path, template_path, new_destination, basepath)
        if os.path.isfile(current_path):
            print(f"Creating file in: {current_path}")
            correct_name = item.split(".")[0] + ".html"
            generate_page(current_path, template_path, os.path.join(destination, correct_name), basepath)

def main():
    from copy import copy_to_docs 
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"
    copy_to_docs("static")
    generate_page_recursively("content", "template.html", "docs", base_path)

if __name__ == "__main__":
    main()
