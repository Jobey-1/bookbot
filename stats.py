def count_book_words(text):
    word_count_list = text.split()
    word_count = len(word_count_list)
    return word_count

def count_book_characters(text):
    text_count = text.lower()
    character_count = {}
    for characters in text_count:
        if characters in character_count:
            character_count[characters] += 1
        else:
            character_count[characters] = 1
    return character_count

def sorted_dictionary_list(dictionary_input):
    new_dictionary = dictionary_input
    dictionary = []
    for i, v in new_dictionary.items():
        dictionary.append({"char": i, "num": v})
    dictionary.sort(reverse=True, key=sort_on)
    return dictionary

def sort_on(items):
    return items["num"]