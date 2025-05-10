from stats import get_num_words, count_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    char_counts = count_characters(text)
    print("Character frequencies:")
    print(char_counts)
    
if __name__ == '__main__':
    main()