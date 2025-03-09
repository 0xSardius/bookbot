from stats import word_count, char_count, sorted_char_count
import sys

file_path = sys.argv[1]

if len(sys.argv) < 2 :
    print("Usage: python main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath) :
    with open(filepath) as f :
        book_contents = f.read()
    return book_contents

def main() :
    # generate relative path to frankenstein.txt
    book_text = get_book_text(file_path)
    total_words = word_count(book_text)
    sorted_chars = sorted_char_count(char_count(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char, count in sorted_chars.items():
        print(f"{char}: {count}")
    
    print("============= END ===============")



if __name__ == "__main__" :
    main()