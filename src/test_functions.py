import unittest

from functions import extract_markdown_images, extract_markdown_links, extract_title


class TestFunctions(unittest.TestCase):
    def test_extract_markdown_images_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extract_markdown_images(text), expected)

    
    def test_extract_markdown_images_2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected)

    
    def test_extract_markdown_images_no_matches(self):
        text = "This is text with no images"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)


    def test_extract_markdown_links_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(extract_markdown_links(text), expected)


    def test_extract_markdown_links_2(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected)


    def test_extract_markdown_links_no_matches(self):
        text = "This is text with a link"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)


    def test_extract_markdown_links_no_match_on_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)

    
    def test_extract_title_1(self):
        markdown = "# heading"
        result = extract_title(markdown)
        self.assertEqual(result, "heading")

    
    def test_extract_title_2(self):
        markdown = "# heading\n\n## sub-heading\n\nparagraph"
        result = extract_title(markdown)
        self.assertEqual(result, "heading")

    
    def test_extract_title_exception(self):
        markdown = "## sub-heading\n\nparagraph"
        self.assertRaises(Exception, lambda: extract_title(markdown))


if __name__ == "__main__":
    unittest.main()