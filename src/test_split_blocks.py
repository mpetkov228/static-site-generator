import unittest

from split_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_1(self):
        markdown = "# This is a heading"
        blocks = markdown_to_blocks(markdown)

        self.assertEqual(len(blocks), 1)

        self.assertEqual(blocks[0], "# This is a heading")


    def test_markdown_to_blocks_2(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.     

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        blocks = markdown_to_blocks(markdown)

        self.assertEqual(len(blocks), 3)

        self.assertEqual(blocks[0], "# This is a heading")


if __name__ == "__main__":
    unittest.main()