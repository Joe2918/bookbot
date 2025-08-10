def get_book_text(path):
    with open(path[1]) as f:
        return f.read()

def count_words(book):
    words_list = book.split()
    return len(words_list)

def count_characters(book=str):
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                   "j", "k", "l", "m", "n", "o", "p", "q", "r",
                     "s", "t", "u", "v", "w", "x", "y", "z"]
    characters_dict = {}
    book = book.lower()
    for character in characters:
        characters_dict[character] = book.count(character)
    return characters_dict

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
