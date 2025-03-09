from stats import word_count, char_count

def get_book_text(filepath) :
    with open(filepath) as f :
        book_contents = f.read()
    return book_contents

def main() :
    # generate relative path to frankenstein.txt
    book_text = get_book_text("./books/frankenstein.txt")
    word_count(book_text)
    print(char_count(book_text))

if __name__ == "__main__" :
    main()