import unittest

from convert_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_split_nodes_basic(self):
        node = TextNode("This is text with a `code block word`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [TextNode("This is text with a ", TextType.TEXT, None), TextNode("code block word", TextType.CODE, None)]
        self.assertEqual(new_nodes, answer)
    
    def test_split_nodes_whole(self):
        node = TextNode("`This is text with a code block word`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [(TextNode("This is text with a code block word", TextType.CODE, None))]
        self.assertEqual(new_nodes, answer)

    def test_split_nodes_multiple(self):
        node = TextNode("`Code Block` with `code block` a `code block word`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [TextNode("Code Block", TextType.CODE, None), TextNode(" with ", TextType.TEXT, None) , TextNode("code block", TextType.CODE, None), 
                  TextNode(" a ", TextType.TEXT, None), TextNode("code block word", TextType.CODE, None)]
        self.assertEqual(new_nodes, answer)

    def test_split_nodes_none(self):
        node = TextNode("This is text with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        answer = [(TextNode("This is text with a code block word", TextType.TEXT, None))]
        self.assertEqual(new_nodes, answer)

    def test_split_nodes_error(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        
    def test_split_nodes_multiple(self):
        node = TextNode("This **bolded text** with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        bolded_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        answer = [TextNode("This ", TextType.TEXT, None), TextNode("bolded text", TextType.BOLD, None), TextNode(" with a ", TextType.TEXT, None), TextNode("code block", TextType.CODE, None), 
                  TextNode(" word", TextType.TEXT, None)]
        self.assertEqual(bolded_nodes, answer)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_none(self):
        node = TextNode(
            "This is text with an https://i.imgur.com/zjjcJKZ.png and another second image(https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
            "This is text with an https://i.imgur.com/zjjcJKZ.png and another second image(https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINKS, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINKS, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links_none(self):
        node = TextNode(
            "This is text with an image](https://i.imgur.com/zjjcJKZ.png) and another ![second image(https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
            "This is text with an image](https://i.imgur.com/zjjcJKZ.png) and another ![second image(https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
            ],
            new_nodes,
        )
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a " \
        "`code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
           
        ], 
            new_nodes
    )


if __name__ == "__main__":
    unittest.main()