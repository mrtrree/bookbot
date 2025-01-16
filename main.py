# Counts characters and words in a book and prints a report
def main(book):
    print(f"--- Begin report of {book} ---")
    print(f"{count_words(book)} words found in the document")
    count_characters(book)
    print("--- End Report ---")


def open_txt(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def count_words(book):
    book_text = open_txt(book)
    word_list = []
    word_list = book_text.split()
    word_count = len(word_list)
    return(word_count)


def count_characters(book):
    book_text = open_txt(book).lower()
    character_count = {}
    for l in book_text:
        if l not in character_count:
            character_count[l] = 1
        else:
            character_count[l] = character_count[l] + 1
    for i in character_count:
        print(f"The {i} character was found {character_count[i]} times")


main("books/frankenstein.txt")