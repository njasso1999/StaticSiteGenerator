import unittest
from blocktohtml import markdown_to_html

class TestBlockToHTML(unittest.TestCase):
    def test_block_to_html(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                        

```This is code```

> This is a quote
> This is a quote on line 2

1. one
2. two
3. three                        


* This is the first list item in a list block
- This is a list item
* This is another list item"""

        result = """<div>
    <h1>
        This is a heading
    </h1>
    <p>
        This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.
    </p>
    <pre>
        <code>This is code</code>
    </pre>
    <blockquote>
        This is a quote
        This is a quote on line 2
    </blockquote>
    <ol>    
        <li>
            one
        </li>
        <li>
            two
        </li>
        <li>
            three
        </li>
    </ol>
    <ul>    
        <li>
            This is the first list item in a list block
        </li>
        <li>
            This is a list item
        </li>
        <li>
            This is another list item
        </li>
    </ul>
</div>"""
    
        self.assertEqual(markdown_to_html(text).format_html(), result)