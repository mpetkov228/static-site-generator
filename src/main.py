import os
import shutil

from textnode import TextType, TextNode


def copy_files(src, src_contents, dst):
    for contents in src_contents:
        path = os.path.join(src, contents)
        if os.path.isfile(path):
            shutil.copy(path, dst)
            continue
        new_dst = os.path.join(dst, contents)
        os.mkdir(new_dst)

        new_src = os.path.join(path)
        new_contents = os.listdir(path)
        copy_files(new_src, new_contents, new_dst)


def generate_public():
    public_path = "./public"
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    os.mkdir("public")

    static_path = "./static"
    static_contents = os.listdir("./static")
    copy_files(static_path, static_contents, public_path)


def main():
    my_node = TextNode("text", TextType.TEXT, "www.website.com")
    print(my_node)
    generate_public()


main()