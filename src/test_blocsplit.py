import unittest
from blocksplit import markdown_to_blocks, block_to_block_type, BlockType


class TestBlockSplit(unittest.TestCase):
    def test_split_eq(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        self.assertEqual(markdown_to_blocks(text), ['# This is a heading', 'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.', '- This is the first list item in a list block\n- This is a list item\n- This is another list item'])

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

        def test_block_to_blocktype(self):
            block1 = "```code```"
            block2 = "- code\n- code\n- code"
            block3 = "1. code\n2. code\n3. code"
            block4 = "# code"
            block5 = "> code"
            block6 = "code"
            self.assertEqual(block_to_blocktype(block6, BlockType.PARAGRAPH))
            self.assertEqual(block_to_blocktype(block1, BlockType.CODE))
            self.assertEqual(block_to_blocktype(block2, BlockType.UNORDERED_LIST))
            self.assertEqual(block_to_blocktype(block3, BlockType.ORDERED_LIST))
            self.assertEqual(block_to_blocktype(block4, BlockType.HEADING))
