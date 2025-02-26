class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        children = ""
        content = self.value
        if self.children:
            for child in self.children:
                children += child.to_html()
            content = children
        return f"<{self.tag}{self.props_to_html()}>{content}</{self.tag}>"
        
    

    def props_to_html(self):
        props_string = ""
        if not self.props:
            return props_string
        for key in self.props:
            props_string += f' {key}="{self.props[key]}"'
        return props_string
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        self.value = value

    
    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag field")
        if not self.children:
            raise ValueError("missing children field")
        
        children = ""
        for child in self.children:
            children += child.to_html()
        
        return f'<{self.tag}{self.props_to_html()}>{children}</{self.tag}>'


class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, props=props)

    
    def to_html(self):
        if self.value is None:
            raise ValueError("missing object value")
        if not self.tag:
            return str(self.value)
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'