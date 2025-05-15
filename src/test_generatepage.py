import unittest

from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = """
hello

# header
"""
        title = extract_title(md)
        self.assertEqual(title, "header")
    
    def test_extract_no_title(self):
        md = """
hello

## header
"""
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()