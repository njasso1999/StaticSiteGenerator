

class HTMLNode:
    def __init__(self = None, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        if self.props:
            for items in list(self.props.items()):
                result += f' {items[0]}="{items[1]}"'
        return result
    
    def ___repr___(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __str__(self):
        return self.___repr___()
    
