import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("<p>", props={"id": "main", "class": "red"})
        string = ' id="main" class="red"'
        self.assertEqual(node.props_to_html(), string)

    
    def test_props_to_html_2(self):
        node = HTMLNode("<a>", props={"href": "http://example.com", "target": "_blank"})
        string = ' href="http://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), string)

    
    def test_props_to_html_3(self):
        node = HTMLNode("<h1>", props={"class": "main-heading"})
        string = ' class="main-heading"'
        self.assertEqual(node.props_to_html(), string)

    
    def test_props_to_html_no_props(self):
        node = HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")


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


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "paragraph", props={"id": "first"})
        string = '<p id="first">paragraph</p>'
        self.assertEqual(node.to_html(), string)
    

    def test_to_html_error(self):
        node = LeafNode("p")
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()