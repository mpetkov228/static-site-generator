import os
import shutil

from gen_page import generate_page


def copy_files(src, src_contents, dst):
    for contents in src_contents:
        from_path = os.path.join(src, contents)
        to_path = os.path.join(dst, contents)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
            print(f"Copying {from_path} to {to_path}")
            continue
        new_dst = os.path.join(dst, contents)
        os.mkdir(new_dst)

        new_src = os.path.join(from_path)
        new_contents = os.listdir(from_path)
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
    generate_public()
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()