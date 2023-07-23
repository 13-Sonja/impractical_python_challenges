"""Count and display all the letters of an input string in lower case."""

import pprint
from collections import defaultdict
import string

letters = defaultdict(list)
sentence = input("Enter a sentence in any language: ").lower()

for letter in sentence:
    letters[letter].append(letter) if letter in string.ascii_lowercase else None

for letter in string.ascii_lowercase:
    if letter not in letters[letter]:
        letters[letter] = ""
# results = sorted(letters.items(), key=lambda x: len(x[1]), reverse=True)

print("\nAll the letters in your sentence:")
pprint.pprint(letters, width=110)
