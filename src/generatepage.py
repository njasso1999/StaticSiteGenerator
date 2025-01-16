import os

from extracttitle import extract_title
from markdownblocks import markdown_to_html_node

def generate_page(from_path, template_path, destination_path):
    print(f"Generating page from {from_path} to {destination_path} with {template_path}")
    with open(f"{from_path}", "r") as f:
        markdown_file = f.read()
    with open(f"{template_path}", "r") as f:
        template = f.read()
    html = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    directory = os.path.dirname(destination_path)
    directories = directory.split("/")
    path = ""
    for dir in directories:
        path = os.path.join(path, dir)
        if os.path.exists(path):
            continue
        else:
            os.makedirs(path)
    with open(f"{destination_path}", "w") as f:
        f.write(page)
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content):
        content = dir_path_content.split("/")[0]
        dest_directory = os.path.join(os.path.dirname(dir_path_content).replace(content, dest_dir_path), "index.html")
        generate_page(dir_path_content, template_path, dest_directory)
        return
    directory_list = os.listdir(dir_path_content)
    for file in directory_list:
        generate_page_recursive(os.path.join(dir_path_content, file), template_path, dest_dir_path)
        

    