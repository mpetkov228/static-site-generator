def markdown_to_blocks(markdown):
    lst = markdown.split("\n\n")
    lst_no_whitespace = map(lambda bl: bl.strip(), lst)
    lst_no_empty_blocks = filter(lambda bl: bl != "", lst_no_whitespace)
    return list(lst_no_empty_blocks)