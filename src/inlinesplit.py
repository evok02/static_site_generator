from textnode import TextType, TextNode
from extract import extract_images, extract_links

def split_node_delimiter(nodes, delimiter, text_type):
    converted_nodes = []
    for node in nodes:
        new_nodes = []
        if node.text_type != TextType.PLAIN:
            converted_nodes.append(node)
            continue
        splitted = node.text.split(delimiter)
        if len(splitted) % 2 == 0:
            raise RuntimeError(f"Couldn't find the delimeter in the node: {node}")
        for i, item in enumerate(splitted):
            if item == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(item, TextType.PLAIN))
            else:
                new_nodes.append(TextNode(item, text_type))
        converted_nodes.extend(new_nodes)
    return converted_nodes

def split_node_link(nodes):
    new_nodes = []
    for node in nodes:
        local_nodes = []
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        if not extract_links(node.text):
            new_nodes.append(node)
            continue
        local_links = extract_links(node.text)
        node_text = node.text
        while len(local_links) > 0:
            link = local_links.pop(0)
            content = node.text.split(link[0]+link[1])
            local_nodes.append(TextNode(content[0], TextType.PLAIN))
            local_nodes.append(TextNode(link[0][1:-1], TextType.LINK, link[1][1:-1]))
            if len(content) >= 2:
                node_text = content[1]
        new_nodes.extend(local_nodes)
        if len(node_text) > 0:
            new_nodes.append(TextNode(f"{node_text}", TextType.PLAIN))
    return new_nodes

def split_node_image(nodes):
    new_nodes = []
    for node in nodes:
        local_nodes = []
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        if not extract_images(node.text):
            new_nodes.append(node)
            continue
        local_images = extract_images(node.text)
        node_text = node.text
        while len(local_images) > 0:
            image = local_images.pop(0)
            content = node_text.split(image[0]+image[1])
            local_nodes.append(TextNode(content[0], TextType.PLAIN))
            local_nodes.append(TextNode(image[0][2:-1], TextType.IMAGE, image[1][1:-1]))
            if len(content) >= 2:
                node_text = content[1]
        new_nodes.extend(local_nodes)
        if len(node_text) > 0:
            new_nodes.append(TextNode(f"{node_text}", TextType.PLAIN))
    return new_nodes

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.PLAIN)]
    text_nodes = split_node_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_node_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_node_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_node_image(text_nodes)
    text_nodes = split_node_link(text_nodes)
    return text_nodes
