from stats import *
import sys


def main():
    if len(sys.argv) > 1:
        print("Arguments:", sys.argv[1:])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_char = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_char)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
