from stats import *
import sys

# get text of a book from file stored locally
def get_book_text():
    file_text = None

    # ensures path is passed by user
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    # opens text file and returns as variable
    with open(path) as f:
        file_text = f.read()
    return file_text

def main():
    book_text = get_book_text()
    num_words = count_words_temp(book_text)
    letter_count = count_characters(book_text)
    sorted_characters = sort_character_dict(letter_count)

    path = sys.argv[1]

# print message
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_characters:
            print(f"{item['letter']}: {item['count']}")
    
    print("============= END ===============")

main()