import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_html(self):
        node1 = ParentNode("p", [
            LeafNode("test")
        ])

        node2 = ParentNode("p", [
            LeafNode("test")
        ], 
        {
            "class": "test"
        })

        self.assertEqual(node1.to_html(), "<p>test</p>")
        self.assertEqual(node2.to_html(), '<p class="test">test</p>')

    def test_no_tag(self):
        node = ParentNode(children=[
            LeafNode("test")
        ])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()