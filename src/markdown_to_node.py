from htmlnode import HTMLNode
from block import BlockType, block_to_blocktype
from split_nodes import text_to_children
from split_blocks import markdown_to_blocks


def paragraph_block_to_html_node(block):
    children = text_to_children(block)
    return HTMLNode("p", None, children)


def heading_block_to_html_node(block):
    heading_size = len(block)-len(block.lstrip("#"))
    heading_text = block.lstrip("#").lstrip()
    nodes = text_to_children(heading_text)
    return HTMLNode(f"h{heading_size}", None, nodes)


def unordered_list_to_html_node(block):
    list_items = list(map(lambda item: item[2:], block.split("\n")))
    list_item_nodes = list(map(lambda item: HTMLNode("li", None, text_to_children(item)), list_items))
    ul = HTMLNode("ul", None, list_item_nodes)
    return ul


def ordered_list_to_html_node(block):
    list_items = list(map(lambda item: item[3:], block.split("\n")))
    list_item_nodes = list(map(lambda item: HTMLNode("li", None, text_to_children(item)), list_items))
    ol = HTMLNode("ol", None, list_item_nodes)
    return ol


def quote_to_html_node(block):
    lines = block.split("\n")
    lines = list(map(lambda line: line.lstrip("> "), lines))
    # lines = list(filter(lambda line: line != "", lines))
    nodes = " ".join(lines)
    return HTMLNode("blockquote", None, text_to_children(nodes))


def code_to_html_node(block):
    code = HTMLNode("code", block[3:-3])
    return HTMLNode("pre", None, [code])


def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_block_to_html_node(block)
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
    
    return HTMLNode("div", None, nodes)