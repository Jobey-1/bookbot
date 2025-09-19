def get_book_text(file_path):
    file_contents = file_path.read()
    return file_contents

def main():
    with open("books/frankenstein.txt") as f:
        return print(get_book_text(f))

main()