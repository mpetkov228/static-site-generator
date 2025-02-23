import unittest

from htmlnode import LeafNode


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