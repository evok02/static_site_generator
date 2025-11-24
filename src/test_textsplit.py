import unittest
from textnode import TextNode, TextType
from inlinesplit import split_node_delimiter, split_node_image, split_node_link


class TestTextSplit(unittest.TestCase):
    def test_split_eq(self):
        nodes1 = [
            TextNode("Some text `code` some text", TextType.PLAIN),
            TextNode("Some text `code` some text", TextType.PLAIN)]
        nodes2 = [
            TextNode("Some text **code** some text", TextType.PLAIN),
            TextNode("Some text **code** some text", TextType.PLAIN)]
       
        nodes3 = [
            TextNode("Some text _code_ some text", TextType.PLAIN),
            TextNode("Some text _code_ some text", TextType.PLAIN)]


        self.assertEqual(split_node_delimiter(nodes1, "`", TextType.CODE), [
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.CODE), 
            TextNode(" some text", TextType.PLAIN),
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.CODE), 
            TextNode(" some text", TextType.PLAIN)
        ])
        self.assertEqual(split_node_delimiter(nodes2, "**", TextType.BOLD), [
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.BOLD),
            TextNode(" some text", TextType.PLAIN),
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.BOLD),
            TextNode(" some text", TextType.PLAIN)
        ])
        self.assertEqual(split_node_delimiter(nodes3, "_", TextType.ITALIC), [
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.ITALIC), 
            TextNode(" some text", TextType.PLAIN),
            TextNode("Some text ", TextType.PLAIN),
            TextNode("code", TextType.ITALIC), 
            TextNode(" some text", TextType.PLAIN)
        ])



