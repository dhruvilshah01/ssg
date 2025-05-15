import unittest
from convert_markdown import markdown_to_html_node


class TestConvertMarkdown(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_unordered_list(self):
        md = """
- Apples
- Bananas
- Cherries
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(
            html,
            "<div><ul><li>Apples</li><li>Bananas</li><li>Cherries</li></ul></div>",
        )
    
    def test_blockquote(self):
        md = """
> This is the first line of a quote.
> This is the second line.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        print("\n",html)
        self.assertEqual(
            html,
            """<div><blockquote>This is the first line of a quote.
This is the second line.</blockquote></div>"""
        )

        

if __name__ == "__main__":
    unittest.main()