import unittest

from parentnode import ParentNode   
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):  
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        child_node = LeafNode("b", "grandchild")
        child_node_2 = LeafNode("span", "child1")
        parent_node = ParentNode("div", [child_node, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>grandchild</b><span>child1</span></div>",
        )
    
    def test_to_html_nested_parents(self):
        child_node = LeafNode("b", "grandchild")
        child_node_2 = LeafNode("span", "child1")
        nested_parent_node = ParentNode("parentnode", [child_node])
        parent_node = ParentNode("div", [child_node, nested_parent_node, child_node_2]) 
        self.assertEqual( 
            parent_node.to_html(),
            "<div><b>grandchild</b><parentnode><b>grandchild</b></parentnode><span>child1</span></div>"
        )
    
    def test_to_html_parents(self):
        child_node = LeafNode("b", "grandchild")
        child_node_2 = LeafNode("span", "child1")
        nested_parent_node = ParentNode("parentnode", [child_node,child_node_2])
        parent_node = ParentNode("div", [nested_parent_node]) 
        self.assertEqual( 
            parent_node.to_html(),
            "<div><parentnode><b>grandchild</b><span>child1</span></parentnode></div>"
        )
    

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    