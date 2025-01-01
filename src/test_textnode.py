import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("url", TextType.BOLD, None)
        node2 = TextNode("url", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("1", TextType.NORMAL)
        node2 = TextNode("2", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        test_cases = [
            TextNode("normal", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode("italics", TextType.ITALIC),
            TextNode("code", TextType.CODE),
            TextNode("link", TextType.LINK, "link.com"),
            TextNode("image", TextType.IMAGE, url="image.com")
        ]

        test_results = [
            "normal",
            "<b>bold</b>",
            "<i>italics</i>",
            "<code>code</code>",
            '<a href="link.com">link</a>',
            '<img src="image.com" alt="image"></img>'
        ]

        for i in range(len(test_cases)):
            self.assertEqual(text_node_to_html_node(test_cases[i]).to_html(), test_results[i])