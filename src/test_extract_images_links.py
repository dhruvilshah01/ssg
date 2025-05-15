import unittest

from convert_nodes import extract_markdown_images, extract_markdown_links

class TestExtractImagesLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is ![text](somewebsite.com) with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual([("text", "somewebsite.com"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images(
            "This is ![text somewebsite.com with an image(https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is [text](somewebsite.com) with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual([("text", "somewebsite.com"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links_none(self):
        matches = extract_markdown_links(
            "This is [text somewebsite.com with an image(https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()