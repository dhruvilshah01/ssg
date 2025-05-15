import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a","google.com",props = {"href": "https://google.com"})
        htmlString = "<a href=\"https://google.com\">google.com</a>"
        self.assertEqual(node.to_html(), htmlString)
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("b",None,None)
        with self.assertRaises(ValueError):
            node.to_html()
    


if __name__ == "__main__":
    unittest.main()