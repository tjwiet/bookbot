def get_word_count(text):
    return len(text.split())

def get_char_counts(text):
    text_lower = text.lower()
    unique_characters = {}

    for char in text_lower:
        if char not in unique_characters:
            unique_characters[char] = 1
        else:
            unique_characters[char] += 1
    return unique_characters

def sort_on(listing: tuple[str, int]):
    return listing[1]

def chars_dict_to_sorted_list(characters: dict[str, int]):
    unsorted_list = []
    for char in characters:
        unsorted_list.append((char, characters[char]))
    return sorted(unsorted_list, reverse = True, key = sort_on)
