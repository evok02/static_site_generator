from textnode import TextType, TextNode
from extract import extract_images, extract_links

def split_node_delimiter(nodes, delimiter, text_type):
    converted_nodes = []
    for node in nodes:
        new_nodes = []
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            raise RuntimeError(f"Couldn't find the delimeter in the node: {node}")
        for i, item in enumerate(node.text.split(delimiter)):
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
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        if not extract_links(node.text):
            new_nodes.append(node)
        local_links = extract_links(node.text)
        node_text = node.text
        while len(local_links) > 0:
            local_nodes = []
            link = local_links.pop(0)
            content = node.text.split(link[0]+link[1])
            local_nodes.append(TextNode(content[0], TextType.PLAIN))
            local_nodes.append(TextNode(link[0][1:-1], TextType.LINK, link[1][1:-1]))
            node_text = node_text[1]
        if content[1]:
            local_nodes.append(content[1])
        new_nodes.extend(local_nodes)
    return new_nodes

def split_node_image(nodes):
    new_nodes = []
    for node in nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        if not extract_images(node.text):
            new_nodes.append(node)
        local_images = extract_images(node.text)
        print(node.text)
        node_text = node.text
        while len(local_images) > 0:
            local_nodes = []
            image = local_images.pop(0)
            content = node_text.split(image[0]+image[1])
            local_nodes.append(TextNode(content[0], TextType.PLAIN))
            local_nodes.append(TextNode(image[0][2:-1], TextType.IMAGE, image[1][1:-1]))
            node_text = node_text[1]
        if content[1]:
            local_nodes.append(content[1])
        new_nodes.extend(local_nodes)
    return new_nodes

