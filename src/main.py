from textnode import TextType, TextNode


def main():
    my_node = TextNode("text", TextType.NORMAL, "www.website.com")
    print(my_node)


main()