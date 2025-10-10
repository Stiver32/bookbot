def count_words(text_from_book):
    words = text_from_book.split() 
    return len(words)


def counting_chars_dict(text_from_book):
    char_counts = {}

    for char in text_from_book:
        lowered_char = char.lower()
        if lowered_char in char_counts:
            char_counts[lowered_char] += 1
        else:
            char_counts[lowered_char] = 1
    return char_counts


def sort_on(items):
    return items['num']

def chars_dict_to_sorted_list(num_chars_dict):

    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


