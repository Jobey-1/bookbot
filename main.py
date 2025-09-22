from stats import count_book_words
from stats import count_book_characters
from stats import sorted_dictionary_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    num_words = count_book_words(book_text)
    letter_count = count_book_characters(book_text)
    sorted_list = sorted_dictionary_list(letter_count)
    nl = "\n"
    header = f"============ BOOKBOT ============{nl}Analyzing book found at {book_file_path}...{nl}----------- Word Count ----------{nl}Found {num_words} total words{nl}--------- Character Count -------"
    footer = "============= END ==============="
    print(header)
    for i in sorted_list:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
        else:
            pass
    print(footer)

main()