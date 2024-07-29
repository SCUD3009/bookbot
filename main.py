def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    character_sortet = character_sort(character_count)
    print (text)
    print(f"{num_words} words found in the document")
    for character in character_sortet:
        print (f"The Letter {character['character']} is found {character['count']} times in the book.")
    #print(character_sortet)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_character_count(text):
    lowered_text = text.lower()
    character_dict = {}
    character_list = []
    for (letter) in lowered_text:
        if (letter).isalpha():
            if letter not in character_dict:
                character_dict[letter]= 1
            else:
                character_dict[letter] += 1
    for character in character_dict:
        char_dict = {}
        count = character_dict[character]
        char_dict["character"] = character
        char_dict["count"] = count
        character_list.append(char_dict)
    return character_list

def sort_key(character_count):
    return character_count["count"]

def character_sort(character_count):
    character_count.sort(reverse=True, key=sort_key)
    return character_count



main()
