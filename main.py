from stats import *
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_character = get_num_character(text)
    sorted = sort(num_character)
    print(
        f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------"""
    )
    for dict in sorted:
        print(f"{dict["char"]}: {dict["num"]}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()