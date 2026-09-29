import sys
from stats import get_word_count, get_char_counts, chars_dict_to_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def print_report(path, word_ct, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_ct} total words")
    print("--------- Character Count -------")
    for char in chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path)
    word_ct = get_word_count(text)
    chars_dict = get_char_counts(text)
    chars = chars_dict_to_sorted_list(chars_dict)
    print_report(path, word_ct, chars)


if __name__ == "__main__":
    main()
