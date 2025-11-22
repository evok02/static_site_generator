import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_attr(self):
        node1 = HTMLNode("p", "This is paragraph")
        self.assertEqual((node1.children, node1.props), (None, None))
        self.assertEqual(node1.tag, "p")
        self.assertEqual(node1.value, "This is paragraph")
        

    def test_props_eq(self):
        node1 = HTMLNode("p", "This is paragraph", props = {
                        "href": "https://www.google.com",
                        "target": "_blank",
                        }) 
        self.assertEqual(node1.props_to_html(),  "href=\"https://www.google.com\" target=\"_blank\"")

    def test_no_props(self):
        node1 = HTMLNode("a", "This is a link")
        self.assertEqual(node1.props_to_html(), "")

    def test_node_to_html(self):
        node1 = LeafNode("p", "This is paragraph", {
                        "href": "https://www.google.com",
                        "target": "_blank",
                        }) 

        node2 = LeafNode(None, "This is paragraph")
        node3 = LeafNode("p", "This is paragraph")
        self.assertEqual(node1.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">This is paragraph</p>")
        self.assertEqual(node2.to_html(), "This is paragraph")
        self.assertEqual(node3.to_html(), "<p>This is paragraph</p>")
    
    def test_parent_eq(self):
        child_node1 = LeafNode("b", "This is bold text")
        child_node2 = LeafNode("i", "This is italic text")
        parent_node1 = ParentNode("p", children = [child_node1, child_node2])
        parent_node2 = ParentNode("p", children = [child_node1, child_node2, child_node1, child_node2])
        self.assertEqual(parent_node1.to_html(), "<p><b>This is bold text</b><i>This is italic text</i></p>")
        self.assertEqual(parent_node2.to_html(), "<p><b>This is bold text</b><i>This is italic text</i><b>This is bold text</b><i>This is italic text</i></p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )



if __name__ == "__main__":
    unittest.main()
