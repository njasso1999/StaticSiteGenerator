from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode needs tag")
        if self.children == None:
            raise ValueError("ParentNode needs children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def format_html(self, tab_num = 0):
        tabs = "    " * tab_num
        tabs2 = tabs
        child_text = ""
        new_line = "\n"
        if self.tag == "div":
            new_line = ""
        for child in self.children:
            if child.__class__ == LeafNode:
                child_text += child.format_html(tab_num + 1)
                tabs2 = tabs + "    "
            elif self.tag == "ol" or self.tag == "ul":
                child_text += "\n" + child.format_html(tab_num + 1)
                new_line = ""
            else:
                child_text += "\n" + tabs + child.format_html(tab_num + 1)
        return f"{tabs}<{self.tag}{self.props_to_html()}>{new_line}{tabs2}{child_text}\n{tabs}</{self.tag}>"