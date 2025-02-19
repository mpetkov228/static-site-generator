from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    
    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag field")
        if not self.children:
            raise ValueError("missing children field")
        
        children = ""
        for child in self.children:
            children += child.to_html()
        
        return f'<{self.tag}{self.props_to_html()}>{children}</{self.tag}>'