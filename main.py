def main():
    bookpath = "books/frankenstein.txt"
    text_from_book = open_book_get_text(bookpath)
    word_count = count_words(text_from_book)
    char_count = count_characters(text_from_book)
    #print(f"The total number of words in '{bookpath}' is {word_count}")
    #print(char_count)
    print(f"######################## This is a report of '{bookpath}' ##########################")
    print(f"This book had {word_count} words")
    print(f"This is a character by character breakdown of this book:")
    character_report(char_count)
    print(f"######################### This is the end of the report for '{bookpath}' #########################")


def open_book_get_text(path_to_book):
    with open(path_to_book) as book:
        book_contents = book.read()
        return book_contents

def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def count_characters(book_text):
    char_dict = {}
    for word in book_text:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def character_report(char_dict):
    sorted_list = []
    for char in char_dict:
        if char.isalpha():
            sorted_list.append((char,char_dict[char]))
    sorted_list.sort()
    for entry in sorted_list:
        print(f"The '{entry[0]}' character was found {entry[1]} times")
    return None
main()
