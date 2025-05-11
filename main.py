import sys

from stats import get_num_words, count_characters, sort_character_counts

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    sorted_counts = sort_character_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

    
if __name__ == '__main__':
    main()