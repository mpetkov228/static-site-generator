import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_1(self):
        node = TextNode("This is text with a ```code block``` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "```", TextType.CODE)
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

    
    # def test_split_nodes_delimiter_unclosed_delimiter(self):
    #     node = TextNode("This is text with a **bold word", TextType.TEXT)
    #     self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "**", TextType.BOLD))


class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image_1(self):
        node = TextNode("Hello ![alt](url) world", TextType.TEXT)
        nodes = split_nodes_image([node])
        
        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "alt")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "url")

        self.assertEqual(nodes[2].text, " world")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)


    def test_split_nodes_image_2(self):
        node = TextNode("Hello ![alt](url) world ![alt2](url2) end", TextType.TEXT)
        nodes = split_nodes_image([node])
        
        self.assertEqual(len(nodes), 5)

        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "alt")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "url")

        self.assertEqual(nodes[2].text, " world ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[3].text, "alt2")
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[3].url, "url2")

        self.assertEqual(nodes[4].text, " end")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)


class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link_1(self):
        node = TextNode("Hello [there](url) world", TextType.TEXT)
        nodes = split_nodes_link([node])
        
        self.assertEqual(len(nodes), 3)

        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "there")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "url")

        self.assertEqual(nodes[2].text, " world")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    
    def test_split_nodes_link_2(self):
        node = TextNode("Hello [alt](url) world [alt2](url2) end", TextType.TEXT)
        nodes = split_nodes_link([node])
        
        self.assertEqual(len(nodes), 5)

        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "alt")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "url")

        self.assertEqual(nodes[2].text, " world ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

        self.assertEqual(nodes[3].text, "alt2")
        self.assertEqual(nodes[3].text_type, TextType.LINK)
        self.assertEqual(nodes[3].url, "url2")

        self.assertEqual(nodes[4].text, " end")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)


class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes_1(self):
        text = "This is **text**"
        nodes = text_to_textnodes(text)
        
        self.assertEqual(len(nodes), 2)

        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)

    
    def test_text_to_textnodes_2(self):
        text = "This is text with **bold** and *italic* nodes"
        nodes = text_to_textnodes(text)

        self.assertEqual(len(nodes), 5)

        self.assertEqual(nodes[0].text, "This is text with ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)

        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)


if __name__ == "__main__":
    unittest.main()