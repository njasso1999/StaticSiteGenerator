import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = str(HTMLNode(tag="only"))
        text = "HTMLNode(tag=only, value=None, children=None, props=None)"
        self.assertEqual(node, text)
    
    def test_props_to_html(self):
        node = HTMLNode(props={"tag": "only"}).props_to_html()
        text = " tag=\"only\""
        self.assertEqual(node, text)

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode().to_html()