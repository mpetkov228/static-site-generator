from textnode import TextNode, TextType, text_node_to_html_node
from functions import extract_markdown_images, extract_markdown_links


# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     if delimiter != "```" and delimiter != "*" and delimiter != "**" and delimiter != "_" and delimiter != "`":
#         raise Exception("unknown delimiter")
    
#     new_nodes = []
#     for node in old_nodes:
#         if node.text == "":
#             continue
#         if delimiter not in node.text:
#             new_nodes.append(node)
#             continue

#         parts = node.text.split(delimiter)
#         print(parts)
#         if len(parts) < 2:
#             raise Exception("missing closing delimiter")
        
#         for i in range(len(parts)):
#             if i == 1:
#                 new_nodes.append(TextNode(parts[1], text_type))
#             else:
#                 new_nodes.append(TextNode(parts[i], TextType.TEXT))
#     print(new_nodes)
#     return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        nodes = []
        for tup in matches:
            parts = text.split(f"![{tup[0]}]({tup[1]})")
            if parts[0] != "":
                nodes.append(TextNode(parts[0], TextType.TEXT))
            nodes.append(TextNode(tup[0], TextType.IMAGE, tup[1]))
            text = "".join(parts[1:])
        
        if text != "":
            nodes.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(nodes)
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        nodes = []
        for tup in matches:
            parts = text.split(f"[{tup[0]}]({tup[1]})")
            if parts[0] != "":
                nodes.append(TextNode(parts[0], TextType.TEXT))
            nodes.append(TextNode(tup[0], TextType.LINK, tup[1]))
            text = "".join(parts[1:])
        
        if text != "":
            nodes.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(nodes)
    
    return new_nodes


def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    nodes_bold = split_nodes_delimiter(node, "**", TextType.BOLD)
    nodes_italic = split_nodes_delimiter(nodes_bold, "*", TextType.ITALIC)
    nodes_italic = split_nodes_delimiter(nodes_italic, "_", TextType.ITALIC)
    nodes_code = split_nodes_delimiter(nodes_italic, "```", TextType.CODE)
    nodes_code = split_nodes_delimiter(nodes_code, "`", TextType.CODE)
    nodes_image = split_nodes_image(nodes_code)
    nodes_link = split_nodes_link(nodes_image)
    return nodes_link


def text_to_children(text):
    nodes = text_to_textnodes(text)
    htmlnodes = list(map(lambda node: text_node_to_html_node(node), nodes))
    return htmlnodes