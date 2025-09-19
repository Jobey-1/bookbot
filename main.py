def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_book_words(text):
    word_count_list = text.split()
    word_count = len(word_count_list)
    return word_count

def main():
    book_file_path = "books/frankenstein.txt"
    book_text = get_book_text(book_file_path)
    num_words = count_book_words(book_text)
    print(f"{num_words} words found in the document")
    
main()