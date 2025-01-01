import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode().to_html()

    def test_only_value(self):
        node = LeafNode(value="only")
        self.assertEqual(node.to_html(), "only")

    def test_tag_without_props(self):
        node = LeafNode(tag="p", value="only")
        self.assertEqual(node.to_html(), "<p>only</p>")

    def test_tag_with_props(self):
        node = LeafNode(tag="p", value="only", props={"class": "single"})
        self.assertEqual(node.to_html(), '<p class="single">only</p>')
