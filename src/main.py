from statictopublic import static_to_public
from generatepage import generate_page_recursive

def main():
    static_to_public("./static")
    generate_page_recursive("context", "template.html", "public")
    

main()