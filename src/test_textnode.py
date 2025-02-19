import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node type italic", TextType.ITALIC)
        self.assertNotEqual(node, node2)


    def test_url_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)


    def test_text_node_to_html_node_text(self):
        node = TextNode("Node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        string = "Node"
        self.assertEqual(html_node.to_html(), string)


    def test_text_node_to_html_node_bold(self):
        node = TextNode("Node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        string = "<b>Node</b>"
        self.assertEqual(html_node.to_html(), string)

    
    def test_text_node_to_html_node_italic(self):
        node = TextNode("Node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        string = "<i>Node</i>"
        self.assertEqual(html_node.to_html(), string)

    
    def test_text_node_to_html_node_code(self):
        node = TextNode("Node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        string = "<code>Node</code>"
        self.assertEqual(html_node.to_html(), string)

    
    def test_text_node_to_html_node_italic(self):
        node = TextNode("Node", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        string = '<a href="http://example.com">Node</a>'
        self.assertEqual(html_node.to_html(), string)


    def test_text_node_to_html_node_image(self):
        node = TextNode("Node", TextType.IMAGE, "http://example.com")
        html_node = text_node_to_html_node(node)
        string = '<img src="http://example.com" alt="Node"></img>'
        self.assertEqual(html_node.to_html(), string)


if __name__ == "__main__":
    unittest.main()