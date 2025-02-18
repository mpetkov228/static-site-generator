class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError("not implemented")
    

    def props_to_html(self):
        props_string = ""
        if not self.props:
            return props_string
        for key in self.props:
            props_string += f' {key}="{self.props[key]}"'
        return props_string
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"