"""Find palindromes recursively."""
import random
import load_files


def find_palindromes(word):
    """Determine if a word is a palindrome."""
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and find_palindromes(word[1:-1])


def main():
    """Load a wordlist and search for palindromes within."""
    words = load_files.open_file("words_list.txt")
    for word in words:
        if find_palindromes(word) and len(word) > 1:
            print(word)


if __name__ == "__main__":
    main()
