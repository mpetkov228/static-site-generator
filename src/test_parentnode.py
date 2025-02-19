import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_one_child(self):
        node = ParentNode("p", [LeafNode("b", "Bold text")])
        string = "<p><b>Bold text</b></p>"
        self.assertEqual(node.to_html(), string)


    def test_to_html_multiple_children(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text")
        ])
        string = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), string)


    def test_to_html_with_parent_node(self):
        node = ParentNode("div", [ParentNode("p", [LeafNode("b", "Bold text")])])
        string = "<div><p><b>Bold text</b></p></div>"
        self.assertEqual(node.to_html(), string)

    
    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()