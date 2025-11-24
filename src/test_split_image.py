import unittest
from inlinesplit import split_node_image, split_node_link
from textnode import TextType

class TestSplitImage(unittest.TestCase):
    def split_link_eq(self):
        nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) text", TextType.PLAIN),
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) text", TextType.PLAIN),
        ]

        print(split_node_link(nodes))
        self.assertEqual(split_node_link(nodes), [
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN),
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN)
        ])

    def split_image_eq(self):
        nodes = [
            TextNode("This is text with a link ![to boot dev](https://www.boot.dev) text", TextType.PLAIN),
            TextNode("This is text with a link ![to boot dev](https://www.boot.dev) text", TextType.PLAIN),
        ]
        print(split_node_image(nodes))
        self.assertEqual(split_node_image(nodes), [
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN),
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" text", TextType.PLAIN)
        ])

        
