import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()