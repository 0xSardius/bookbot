def word_count(text) :
    # split the text into words
    words = text.split()

    # count the number of words
    word_count = len(words)

    print(f"{word_count} words found in the document")

    return word_count

def char_count(text) :
    char_dict = {}
    clean_text = text.lower()
    for char in clean_text :
        if char.isalpha() :
            if char in char_dict :
                char_dict[char] += 1
            else :
                char_dict[char] = 1

    return char_dict

def sorted_char_count(text) :
    values_list = list(text.items())
    values_list.sort(key=lambda x: x[1], reverse=True)
    sorted_dict = dict(values_list)
    return sorted_dict