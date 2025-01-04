import re

def split_blocks(text):
    items = text.split("\n\n")
    blocks = []
    for item in items:
        stripped = item.strip()
        if stripped:
            blocks.append(stripped)

    return blocks

def block_to_block_type(block):
    if bool(re.fullmatch(r"#{1,6} .*", block)):
        return "heading"
    
    if bool(re.fullmatch(r"```.*```$", block)):
        return "code"
    
    if bool(re.fullmatch(r"(> .+[\s\S])+", block)):
        return "quote"
    
    if bool(re.fullmatch(r"([-|\*] .+[\s\S])+", block)):
        return "unordered_list"
    
    if block.startswith("1. "):
        lines = block.split("\n")
        num = 1
        for line in lines:
            if not line.startswith(f"{num}. "):
                return "paragraph"
            num += 1
        return "ordered_list"
    return "paragraph"