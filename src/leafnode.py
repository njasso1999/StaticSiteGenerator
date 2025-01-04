from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value = None, tag = None, props = None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have value")
        opentag = ""
        closetag = ""
        props = self.props_to_html()
        if self.tag:
            opentag = f"<{self.tag}{props}>"
            closetag = f"</{self.tag}>"
        return opentag + self.value + closetag
    
    def format_html(self, tab_num):
        tabs = "    " * tab_num
        html = self.to_html()
        text = html.split("\n")
        text = f"\n{tabs}".join(text)
        return text