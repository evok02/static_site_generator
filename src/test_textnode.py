import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node1, node2)

    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "www.google.com")
        self.assertNotEqual(node1, node2)

    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node1.url, None)

    def test_text(self):
        node2 = TextNode("This is a bold node", TextType.BOLD)
        node3 = TextNode("This is a link", TextType.LINK, "www.google.com")
        node4 = TextNode("Just Image", TextType.LINK, "www.gallery.com") 
        converted2 = node2.text_node_to_html()
        converted3 = node3.text_node_to_html()
        converted4 = node4.text_node_to_html()
        self.assertEqual(node2.text, converted2.value)
        self.assertEqual(node3.text, converted3.value)
        self.assertEqual(node4.text, converted4.value)

if __name__ == "__main__":
    unittest.main()
