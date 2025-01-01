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
            