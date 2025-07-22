import sys
from stats import number_of_words, number_of_characters, sorted_list

def main():
    path = arguments()
    book_text = (get_book_text(path))
    num_words = number_of_words(book_text)
    num_char = number_of_characters(book_text)
    char_list = sorted_list(num_char)
    print_report(path, num_words, char_list)

def arguments():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def print_report(path, num_words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")

    for char in char_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()
