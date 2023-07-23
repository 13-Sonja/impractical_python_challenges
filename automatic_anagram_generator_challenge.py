"""Automatically generates anagram phrases from an input string *VERY* slowly."""
import sys
import random
from collections import Counter
import load_files


def find_anagrams(name, word_list):
    """Finds possible anagrams for the string in a list of english words."""
    name_letters = Counter(name)
    anagrams = []
    for word in word_list:
        temp = ""
        word_letters = Counter(word.lower())
        for letter in word:
            if word_letters[letter] <= name_letters[letter]:
                temp += letter
        if Counter(temp) == word_letters:
            anagrams.append(word)
    return anagrams


def build_phrase(original_name, word_list):
    """Automatically constructs an anagram phrase from the entered string."""
    lenght = len(original_name)
    phrase = ""
    anagrams = find_anagrams(original_name, word_list)
    while len(phrase.replace(" ", "")) != lenght:
        temp_word = random.choice(anagrams)
        phrase += temp_word + " "
        name = "".join(Counter(original_name) - Counter(phrase))
        if not name:
            break
        anagrams = find_anagrams(name, word_list)
        if len(anagrams) == 0:
            phrase = ""
            anagrams = find_anagrams(original_name, word_list)
            continue
    return phrase


def main():
    """Processes the entered string to print resulting anagram phrases."""
    word_list = load_files.open_file("words_list.txt")
    original_word = input(
        "Enter a name you would like to build an anagram phrase from: "
    )
    print("\nThis is going to take a looong time...\n")
    name = "".join(original_word.lower().split())
    name = name.replace("-", "")
    phrases = []
    for _ in range(10):
        phrase = build_phrase(name, word_list)
        phrases.append(phrase.rstrip())

    print(*phrases, sep="\n")


if __name__ == "__main__":
    main()
