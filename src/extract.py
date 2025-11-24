import re

def extract_images(md_text):
    alt = re.findall(r"!\[.*?\]", md_text)
    src = re.findall(r"\(https:.*?\)", md_text)
    return list(zip(alt, src))
    

def extract_links(md_text):
    alt = re.findall(r"\[.*?\]", md_text)
    src = re.findall(r"\(https:.*?\)", md_text)
    return list(zip(alt, src))
