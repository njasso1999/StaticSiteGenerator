import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


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

    def test_split_nodes_delimiter(self):
        test_cases = [
            split_nodes_delimiter(
                [TextNode("**This should be bold** this should not", TextType.NORMAL)],
                "**",
                TextType.BOLD
                ),
            split_nodes_delimiter(
                [TextNode("This is `code` now", TextType.NORMAL)],
                "`",
                TextType.CODE
            ),
            split_nodes_delimiter(
                [TextNode("This should be *italics*", TextType.NORMAL)],
                "*",
                TextType.ITALIC
            ),
            split_nodes_delimiter(
                [
                    TextNode("This node should be partially *italic*", TextType.NORMAL),
                    TextNode("The whole message should be seen with this one", TextType.NORMAL),
                    TextNode("*The whole message should be seen with this one too but it's italic*", TextType.NORMAL)
                ],
                "*",
                TextType.ITALIC
            )
        ]

        result = [
            [
                TextNode("This should be bold", TextType.BOLD),
                TextNode(" this should not", TextType.NORMAL)
            ],
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" now", TextType.NORMAL)
            ],
            [
                TextNode("This should be ", TextType.NORMAL),
                TextNode("italics", TextType.ITALIC)
            ],
            [
                TextNode("This node should be partially ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode("The whole message should be seen with this one", TextType.NORMAL),
                TextNode("The whole message should be seen with this one too but it's italic", TextType.ITALIC)
            ]
        ]

    def test_split_link_nodes(self):
        test_cases = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.NORMAL,
                
            ),
            TextNode(
                "This is text with no link",
                TextType.NORMAL,
            )
        ]

        results = [
            [TextNode("This is text with a link" , 1, None),
            TextNode("to boot dev", 5," https://www.boot.dev"),
            TextNode(" and ", 1, None),
            TextNode("to youtube", 5, "https://www.youtube.com/@bootdotdev")
            ],
            [
                TextNode("This is a test with no link", 1, None)
            ]
        ]

        

    def test_split_nodes_delimiter_error(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter("*error", "*", TextType.ITALIC)