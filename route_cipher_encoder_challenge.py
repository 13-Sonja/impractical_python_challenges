import numpy as np
import sys

"""Encrypt a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows & columns.
Begins encryption at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers means start at top & read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints encrypted message.
"""
# ==============================================================================
# USER INPUT

# the string to be encrypted (type or paste between triple quotes):
message = """we will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter. This text fills up the message."""

# number of columns in the transposition matrix:
COLS = 6

# number of rows in the transposition matrix:
ROWS = 7

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key = """-1 3 -2 6 5 -4"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ==============================================================================

code_words = {
    "batteries": "hounds",
    "vicksburg": "odor",
    "april": "clayton",
    "16": "sweet",
    "grand": "tree",
    "gulf": "owl",
    "forts": "hickory",
    "river": "bailey",
    "25": "multiply",
    "29": "add",
    "admiral": "hermes",
    "porter": "langford",
}


def main():
    print(f"\nMessage to encrypt: {message}")
    print(f"Trying {COLS} columns.")
    print(f"Trying {ROWS} rows.")
    print(f"Trying key: '{key}'")

    processed_text = prepare_message(message)
    validate_cipher_matrix(processed_text)
    key_list = validate_key(key)
    text_matrix = create_text_matrix(processed_text)
    ciphertext = encrypt_message(key_list, text_matrix)
    print(f"\nEncrypted message: {ciphertext}")


def prepare_message(message):
    """Processes the plaintext and returns a list of words."""
    message = message.replace(".", "").lower()
    for word in code_words:
        message = message.replace(word, code_words[word])
    message_words = message.split()
    return message_words


def validate_cipher_matrix(message_words):
    """Checks if entered message can fit into the cols/rows."""
    factors = []
    message_len = len(message_words)
    for i in range(2, message_len):
        if message_len % i == 0:
            factors.append(i)
    print(f"\nLength of message: {message_len}")
    print(f"Acceptable column/row values include: {factors}")

    if ROWS * COLS != message_len:
        sys.exit("\nInput rows or columns not compatible with length of ciphertext!")


def validate_key(key):
    """Checks if the entered key is valid."""
    key_list = [int(i) for i in key.split()]
    if (
        len(key_list) != COLS
        or min(key_list) < -COLS
        or max(key_list) > COLS
        or 0 in key_list
    ):
        sys.exit("\nKey not compatible with matrix!")
    else:
        return key_list


def create_text_matrix(message_words):
    """Creates a roated text matrix from a list of words."""
    text_matrix = [[None] * COLS] * ROWS
    start = 0
    stop = COLS
    for i in range(ROWS):
        col_items = message_words[start:stop]
        text_matrix[i] = col_items
        start += COLS
        stop += COLS
    rotated_text_matrix = np.rot90(list(reversed(text_matrix)), k=3)
    return rotated_text_matrix


def encrypt_message(key_list, rotated_text_matrix):
    """Encrypts the rotated text matrix with the key."""
    scrambled_matrix = [None] * COLS

    for key, row in zip(key_list, rotated_text_matrix):
        scrambled_matrix[abs(key) - 1] = row
    for idx, key in enumerate(key_list):
        if key < 0:
            scrambled_matrix[idx] = list(reversed(scrambled_matrix[idx]))

    ciphertext = ""
    for row in scrambled_matrix:
        for word in row:
            ciphertext += word + " "
    return ciphertext


if __name__ == "__main__":
    main()
