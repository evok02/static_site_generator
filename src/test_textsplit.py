import unittest
from textnode import TextNode, TextType
from inlinesplit import split_node_delimiter, split_node_image, split_node_link


class TestTextSplit(unittest.TestCase):
    def split_eq(self):
        nodes1 = [
            TextNode("Some text `code` some text", TextType.PLAIN),
            TextNode("Some text `code` some text", TextType.PLAIN)
        ]
        nodes2 = [
            TextNode("Some text **code** some text", TextType.PLAIN),
            TextNode("Some text **code** some text", TextType.PLAIN)
        ]
        nodes3 = [
            TextNode("Some text _code_ some text", TextType.PLAIN),
            TextNode("Some text _code_ some text", TextType.PLAIN)
        ]


        self.assertEqual(split_node_delimeter(nodes1, "`", TextType.CODE), [
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.PLAIN), 
            TextNode("some text", TextType.PLAIN)
        ])
        self.assertEqual(split_node_delimeter(nodes2, "**", TextType.BOLD), [
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.BOLD),
            TextNode("some text", TextType.PLAIN)
        ])
        self.assertEqual(split_node_delimeter(nodes3, "_", TextType.ITALIC), [
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.ITALIC), 
            TextNode("some text", TextType.PLAIN)
        ])

    def split_eq_static(self):
        node = TextNode("code", TextType.ITALIC)
        self.AssertEqual(split_node_delimiter([node], "_", TextType.ITALIC), 
        [TextNode("code", TextType.ITALIC)])


