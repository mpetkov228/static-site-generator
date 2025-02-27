import os

from markdown_to_node import markdown_to_html_node
from functions import extract_title


def read_file(path):
    f = open(path)
    content = f.read()
    f.close()

    return content


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_content = read_file(from_path)
    template_content = read_file(template_path)
    
    title = extract_title(markdown_content)
    html_string = markdown_to_html_node(markdown_content).to_html()
    template_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    dir_name = os.path.dirname(dest_path)
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_contents = os.listdir(dir_path_content)
    for content in dir_contents:
        from_path = os.path.join(dir_path_content, content)
        to_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, to_path.replace(".md", ".html"))
            continue
        generate_pages_recursive(from_path, template_path, to_path)
        
    
    
generate_pages_recursive("./content", "./template.html", "./public")