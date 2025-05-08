def get_num_words(text):
    words = text.split()
    num = 0
    for word in words:
        num += 1
    return num