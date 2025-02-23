import unittest

from block import BlockType, block_to_blocktype


class TestBlock(unittest.TestCase):
    def test_block_to_blocktype_1(self):
        block = "# this is a heading"
        result = block_to_blocktype(block)
        
        self.assertEqual(result, BlockType.HEADING)

    
    def test_block_to_blocktype_2(self):
        block = "```code block```"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.CODE)

    
    def test_block_to_blocktype_3(self):
        block = ">first quote\n>second quote"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.QUOTE)

    
    def test_block_to_blocktype_4(self):
        block = "* one\n* two"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.UNORDERED_LIST)


    def test_block_to_blocktype_5(self):
        block = "1. one\n2. two"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.ORDERED_LIST)


    def test_block_to_blocktype_6(self):
        block = "paragraph"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)


    def test_block_to_blocktype_invalid_1(self):
        block = "#invalid heading"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    
    def test_block_to_blocktype_invalid_2(self):
        block = "```code block"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    
    def test_block_to_blocktype_invalid_3(self):
        block = "1. invalid\n3. list"
        result = block_to_blocktype(block)

        self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()