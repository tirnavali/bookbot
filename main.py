from stats import get_book_text, get_word_count, get_char_count, sort_on
import sys
def main():
    if(len(sys.argv)< 2):
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    
    text = get_book_text(sys.argv[1])
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(text)
    char_count = sort_on(char_count)
    for char in char_count:
        if char.isalpha():
            print(f"{char}: {char_count[char]}")
    
    print("============= END ===============")
if __name__ == "__main__":
    main()