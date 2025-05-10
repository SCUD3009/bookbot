from stats import *


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_character = get_num_character(text)
    #print(text) removed for no wall of text every time
    print(
        f"{num_words} words found in the document.\n", 
        f"Used Characters:{num_character}"
          )


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()