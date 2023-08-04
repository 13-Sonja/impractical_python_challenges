"""Generate new words by recombining letters using Markov models."""
import logging
from collections import defaultdict
from string import ascii_lowercase
import random


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="newword_basic.log",
)

# list of two-letter-pairs to be rejected as starting letters of a word
first_pair_rejects = [
    "ld",
    "lm",
    "lt",
    "lv",
    "rd",
    "rl",
    "rm",
    "rt",
    "rv",
    "tl",
    "tm",
]


def open_file(file):
    """Return a text file as a set."""
    try:
        with open(file) as file:
            content = set(file.read().split())
            return content
    except FileNotFoundError:
        return []


def add_reject(file, reject):
    """Add rejected letter combinations to a text file."""
    with open(file, "a", newline="") as file:
        file.write(f"{reject}\n")


def map_letters(corpus, amount):
    """Finds all possible suffixes following an existing combination of letters in a list of real words."""
    mapped_letters = defaultdict(list)
    for word in corpus:
        if len(word) < (amount + 1):
            continue
        for idx, letter in enumerate(word):
            if idx < len(word) - (amount):
                key = letter
                for i in range(1, amount):
                    key += word[idx + i]
                suffix = word[idx + amount]
                mapped_letters[key].append(suffix)
    return mapped_letters


def find_matching_letter(prefix, mapped_letters):
    """Returns all possible suffixes for a specific combinations of input letters."""
    suffixes = mapped_letters.get(prefix)
    if suffixes == None:
        logging.debug("Broken prefix: %s", prefix)
        add_reject("forbidden_prefixes.txt", prefix)
        return None
    elif len(suffixes) == 1:
        next_letter = suffixes[0]
    else:
        next_letter = random.choice(suffixes)
    return next_letter


def create_new_word(mapped_to_2, mapped_to_3, mapped_to_4, length, forbidden_prefixes):
    """Invents a new word using previously mapped possible letter combinations."""
    word = []
    while True:
        firsts = random.choice(list(mapped_to_2.keys()))
        if firsts in first_pair_rejects:
            break
        word.extend(firsts)
        next_letter = find_matching_letter("".join(word), mapped_to_2.copy())
        word.append(next_letter)
        next_letter = find_matching_letter("".join(word), mapped_to_3.copy())
        if next_letter == None:
            break
        word.append(next_letter)
        while len(word) < length:
            fragment = "".join(word)
            if fragment[-4:] in forbidden_prefixes:
                return None
            next_letter = find_matching_letter(fragment[-4:], mapped_to_4.copy())
            if next_letter == None:
                return create_new_word(
                    mapped_to_2, mapped_to_3, mapped_to_4, length, forbidden_prefixes
                )
            word.append(next_letter)
        return "".join(word)


def main():
    """Lets user create new words of a chosen length."""
    print("\nWelcome to the wonderous word generator!")
    choice = None
    while not choice:
        choice = input(
            "Please specify how long the new word should be (between 4-18): "
        )
        if not choice.isdigit():
            choice = None
            print("Please enter a valid number!")
        elif int(choice) < 4 or int(choice) > 18:
            choice = None
            print("Please enter a number between 4 and 18!")

    corpus = open_file("words_list.txt")
    mapped_to_2 = map_letters(corpus, 2)
    mapped_to_3 = map_letters(corpus, 3)
    mapped_to_4 = map_letters(corpus, 4)

    forbidden_prefixes = open_file("forbidden_prefixes.txt")

    words = []
    while len(words) < 10:
        word = create_new_word(
            mapped_to_2, mapped_to_3, mapped_to_4, int(choice), forbidden_prefixes
        )
        if word != None:
            words.append(word)
    print("\nHere are 10 unique new words for you:")
    print(*words, sep="\n")


if __name__ == "__main__":
    main()
