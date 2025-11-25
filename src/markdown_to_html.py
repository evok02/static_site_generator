from htmlnode import ParentNode, LeafNode, HTMLNode
from textnode import TextNode, TextType
from blocksplit import BlockType, markdown_to_blocks, block_to_block_type
from inlinesplit import text_to_textnodes 


def block_to_html_node(block_type, text):
    match block_type:
        case BlockType.PARAGRAPH:
            return ParentNode("p", None)
        case BlockType.UNORDERED_LIST:
            children = []
            for line in text.split("\n"):
                line = line.replace("- ", "").strip()
                sub_children = text_to_children(line)
                children.append(ParentNode("li", sub_children))
            return ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            children = []
            for line in text.split("\n"):
                line = line.split(".")[1].strip()
                sub_children = text_to_children(line)
                children.append(ParentNode("li", sub_children))
            return ParentNode("ol", children)
        case BlockType.HEADING:
            before_len = len(text)
            text = text.replace("#", "")
            after_len = len(text)
            sub_children = text_to_children(text.strip())
            return ParentNode(f"h{before_len - after_len}", sub_children)
        case BlockType.QUOTE:
            children = []
            for line in text.split("\n"):
                line = line.strip().replace(">", "")
                children.append(LeafNode(tag = None, value = line.strip()))
            return ParentNode("blockquote", children)
        case BlockType.CODE:
            return ParentNode("code", None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for node in text_nodes:
        html_node = node.text_node_to_html()
        leaf_nodes.append(html_node)
    return leaf_nodes


def markdown_to_html_node(text):
    html_nodes = []
    blocks = markdown_to_blocks(text)
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.CODE:
            html_node = ParentNode("pre", None) 
            html_node.children = [TextNode(block, TextType.CODE).text_node_to_html()]
        elif blocktype == BlockType.ORDERED_LIST or blocktype == BlockType.UNORDERED_LIST:
            html_node = block_to_html_node(blocktype, block)
        elif blocktype == BlockType.QUOTE:
            html_node = block_to_html_node(blocktype, block)
        elif blocktype == BlockType.HEADING:
            html_node = block_to_html_node(blocktype, block)
        else:
            html_node = block_to_html_node(blocktype, block)
            html_node.children = text_to_children(block)
        html_nodes.append(html_node)
    return ParentNode("div", html_nodes).to_html()

