import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestBlock(unittest.TestCase):
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
        
    def test_markdown_to_blocks_code(self):
        
        md = """
This is text that _should_ remain
the **same** even with inline stuff
    """
        
        blocks = markdown_to_blocks(md)
 
        self.assertEqual(
            blocks,
            [
                "This is text that _should_ remain\nthe **same** even with inline stuff"
            ],
        )
    
    def test_block_type_code(self):
        
        md = """```code block type```"""

        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_type_unordered_list(self):
    
        md = """- this is a list\n- with items"""

        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_block_type_ordered_list(self):
    
        md = """1. orderedlist\n2. 2nd item"""

        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
    
    def test_block_type_quote(self):
        md = """>This is a multiline\n>quote by dhruv"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_block_type_paragraph(self):
        md = """>This is a multiline\nquote by dhruv"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_type_heading(self):
        md = """## This is a multilinequote by dhruv"""
        md2 = """###### This is a multiline quote by dhruv"""
        not_heading = """######This is a multiline quote by dhruv"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)
        block_type = block_to_block_type(md2)
        self.assertEqual(block_type, BlockType.HEADING)
        block_type = block_to_block_type(not_heading)
        self.assertEqual(block_type, BlockType.PARAGRAPH)