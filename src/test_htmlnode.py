import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        props = {"hello": "brlalal",
                 "target": "blank"}
        
        htmlNode = HTMLNode(props=props)
        
        expected_output = " hello=\"brlalal\" target=\"blank\""

        self.assertEqual(htmlNode.props_to_html(), expected_output)

    def test_htmlnode_emptyprops(self):
        props = {}
        htmlNode = HTMLNode(props=props)
        
        expected_output = " "

        self.assertEqual(htmlNode.props_to_html(), expected_output)
    
    def test_empty_htmlnode(self):
        htmlNode = HTMLNode()
        self.assertEqual(htmlNode.props_to_html(),"")       
    
    def test_htmlnode_print(self):
        htmlNode = HTMLNode(tag="hello", value="anywhere", 
        children="howdy", props = {"hello": "how are ya"})

        expected_output = f"HTML_NODE(hello, anywhere, howdy, {{\'hello\': \'how are ya\'}})"
        
        self.assertEqual(str(htmlNode), expected_output)
    


if __name__ == "__main__":
    unittest.main()