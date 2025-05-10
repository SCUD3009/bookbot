def get_num_words(text):
    words = text.split()
    num = 0
    for word in words:
        num += 1
    return num


def get_num_character(text):
    l_text = text.lower()
    num_character = {}
    for char in l_text:
        if char not in num_character:
            num_character[char] = 1
        else:
            num_character[char] += 1
    return num_character

def sort_key(dict):
    return dict["num"]

def sort(num_character):
    sorted = []
    for k in num_character:
        char_dict = {}
        num = num_character[k]
        if k.isalpha():
            char_dict["char"] = k
            char_dict["num"] = num
            sorted.append(char_dict)
    sorted.sort(reverse=True, key=sort_key)

    return sorted