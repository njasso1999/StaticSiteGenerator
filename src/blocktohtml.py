from splitblocks import split_blocks, block_to_block_type
from parentnode import ParentNode
from textnode import text_to_text_nodes, text_node_to_html_node

def markdown_to_html(md):
    blocks = split_blocks(md)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                block_split = block.split("# ", 1)
                heading_num = len(block_split[0]) + 1
                text = block_split[1]
                block_children = get_children(text)
                children.append(ParentNode(f"h{heading_num}", block_children))
            case "code":
                block_children = get_children(block)
                children.append(ParentNode("pre", block_children))
            case "quote":
                block_split = block.split("> ")
                text_list = []
                for block in block_split:
                    if block:
                        text_list.append(block)
                text = "".join(text_list)
                block_children = get_children(text)
                children.append(ParentNode("blockquote", block_children))
            case "unordered_list":
                block_children = get_li_children(block)
                children.append(ParentNode("ul", block_children))
            case "ordered_list":
                block_children = get_li_children(block)
                children.append(ParentNode("ol", block_children))
            case "paragraph":
                block_children = get_children(block)
                children.append(ParentNode("p", block_children))
    
    return ParentNode("div", children)
            


def get_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children

def get_li_children(block):
    li_items = block.split("\n")
    children = []
    for li in li_items:
        text = li.split(" ", 1)[1]
        li_children = get_children(text)
        children.append(ParentNode("li", li_children))
    return children
