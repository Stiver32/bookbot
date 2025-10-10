import sys
from stats import (
    count_words,
    chars_dict_to_sorted_list,
    counting_chars_dict,
)


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        # join it with the "books" folder
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        # print(book_text)
        num_words = count_words(book_text)
        chars_dict = counting_chars_dict(book_text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

        print_report(book_path, num_words,chars_sorted_list)


# Get book Text
def get_book_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content 
    except FileNotFoundError:
        raise FileNotFoundError(f"Error, {file_path} not found")
    except IOError as e:
        raise IOError(f"Error reading {file_path}: {e}")
    
    
# Print report function
def print_report(book_path, num_words,chars_sorted_list):
    print("=========BOOKBOT==========")
    print(f"Analyzing book found at {book_path}...")
    print("------------ Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue 
        print(f"{item['char']}: {item['num']}")
    print("===================== END ======================")


# MAIN PROGRAM


main()
