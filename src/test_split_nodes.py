import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        string = "[TextNode(This is text with a , normal, None), TextNode(code block, code, None), TextNode( word, normal, None)]"
        self.assertEqual(str(new_nodes), string)


    def test_split_nodes_delimiter_2(self):
        node = TextNode("This is text with a **bold word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        string = "[TextNode(This is text with a , normal, None), TextNode(bold word, bold, None), TextNode(, normal, None)]"
        self.assertEqual(str(new_nodes), string)

    
    def test_split_nodes_delimiter_3(self):
        node = TextNode("This is text with a *italic word*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        string = "[TextNode(This is text with a , normal, None), TextNode(italic word, italic, None), TextNode(, normal, None)]"
        self.assertEqual(str(new_nodes), string)

    
    def test_split_nodes_delimiter_wrong_delimiter(self):
        node = TextNode("This is text with a **bold word**", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "***", TextType.BOLD))

    
    def test_split_nodes_delimiter_unclosed_delimiter(self):
        node = TextNode("This is text with a **bold word", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "**", TextType.BOLD))


if __name__ == "__main__":
    unittest.main()