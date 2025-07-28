import sys

from stats import count_of_words
from stats import count_of_symbols
from stats import sort_of_symbols_stat

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = count_of_words(text)
    num_symbols = count_of_symbols(text)
    stats = sort_of_symbols_stat(num_symbols)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for stat in stats:
        if not stat["char"].isalpha():
            continue

        print(f"{stat['char']}: {stat['num']}")

    print("============= END ===============")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
