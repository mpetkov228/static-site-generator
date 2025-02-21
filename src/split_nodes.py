from textnode import TextNode, TextType
from functions import extract_markdown_images


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter != "`" and delimiter != "*" and delimiter != "**":
        raise Exception("unknown delimiter")
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) != 3:
            raise Exception("missing closing delimiter")
        
        for i in range(len(parts)):
            if i == 1:
                new_nodes.append(TextNode(parts[1], text_type))
            else:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))

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


node = TextNode(
    "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
node2 = TextNode("Hello ![alt](url) end", TextType.TEXT)
print(split_nodes_image([node]))
print(split_nodes_image([node2]))

def split_nodes_link(old_nodes):
    pass
