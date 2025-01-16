from splitblocks import split_blocks

def extract_title(markdown):
    title = split_blocks(markdown)[0]
    if title[:2] != "# ":
        raise Exception("first line of markdown file must be heading 1 block")
    return title[2:].strip()