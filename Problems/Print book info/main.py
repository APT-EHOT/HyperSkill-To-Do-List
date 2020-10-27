def print_book_info(title, author=None, year=None):
    s = f'"{title}"'
    if author is not None or year is not None:
        s += " was written"
    if author is not None:
        s += f' by {author}'
    if year is not None:
        s += f' in {year}'
    print(s)
