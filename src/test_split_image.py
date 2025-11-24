import unittest
from inlinesplit import split_node_image, split_node_link, text_to_textnodes
from textnode import TextType, TextNode

class TestSplitImage(unittest.TestCase):
    def test_split_link_eq(self):
        nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) text", TextType.PLAIN),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) text", TextType.PLAIN),
        ]

        self.assertEqual(split_node_link(nodes), [
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN),
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN)
        ])

    def test_split_image_eq(self):
        nodes = [
            TextNode("This is text with a link ![to boot dev](https://www.boot.dev) text", TextType.PLAIN),
            TextNode("This is text with a link ![to boot dev](https://www.boot.dev) text", TextType.PLAIN),
        ]
        self.assertEqual(split_node_image(nodes), [
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN),
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN)
        ])

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
    TextNode("This is ", TextType.PLAIN),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.PLAIN),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.PLAIN),
    TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.PLAIN),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])
