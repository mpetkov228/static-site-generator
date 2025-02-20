from textnode import TextNode, TextType

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


# node2 = TextNode("This is text with a **bold word**", TextType.TEXT)
# node3 = TextNode("*Italic* text", TextType.TEXT)
# node4 = TextNode("Italic text 2", TextType.ITALIC)
# print(split_nodes_delimiter([node], "`", TextType.CODE))
# print(split_nodes_delimiter([node2], "**", TextType.BOLD))
# print(split_nodes_delimiter([node3, node4], "*", TextType.ITALIC))