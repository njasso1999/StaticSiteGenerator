import os

from extracttitle import extract_title
from blocktohtml import markdown_to_html

def generate_page(from_path, template_path, destination_path):
    print(f"Generating page from {from_path} to {destination_path} with {template_path}")
    with open(f"{from_path}", "r") as f:
        markdown_file = f.read()
    with open(f"{template_path}", "r") as f:
        template = f.read()
    html = markdown_to_html(markdown_file).to_html()
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
        
        
    