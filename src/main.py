from statictopublic import static_to_public
from generatepage import generate_page

def main():
    static_to_public("./static")
    generate_page("context/index.md", "template.html", "public/index.html")
    

main()