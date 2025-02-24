from split_blocks import markdown_to_blocks
from block import BlockType, block_to_blocktype


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


def heading_block_to_html_node(block):
    heading_size = len(block)-len(block.lstrip("#"))
    heading_text = block.lstrip("#").lstrip()
    return HTMLNode(f"h{heading_size}", heading_text)


def unordered_list_to_html_node(block):
    list_items = list(map(lambda item: item[2:], block.split("\n")))
    list_item_nodes = list(map(lambda item: LeafNode("li", item), list_items))
    ul = ParentNode("ul", list_item_nodes)
    return ul


def ordered_list_to_html_node(block):
    list_items = list(map(lambda item: item[3:], block.split("\n")))
    list_item_nodes = list(map(lambda item: LeafNode("li", item), list_items))
    ol = ParentNode("ol", list_item_nodes)
    return ol


def quote_to_html_node(block):
    pass


def code_to_html_node(block):
    pass


def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return HTMLNode("p", block)
        case BlockType.HEADING:
            return heading_block_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case _:
            raise Exception("invalid block type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        nodes.append(block_to_html_node(block, block_type))
    return nodes


markdown = """
## Header

Paragraph

1. List item
2. List item

>quote
>quote

[link](somewhere)

![image](something)

*italics*

**bold**
"""

print(markdown_to_html_node(markdown))