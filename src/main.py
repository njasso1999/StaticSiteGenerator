from splitblocks import split_blocks, block_to_block_type
from blocktohtml import markdown_to_html
import re

def main():
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
    
    print(markdown_to_html(text).format_html())

main()