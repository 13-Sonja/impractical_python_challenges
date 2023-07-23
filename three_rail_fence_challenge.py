import math
from itertools import zip_longest

"""En- and decrypt a Civil War 'rail fence' type cipher.

This is for a "3-rail" fence cipher for short messages

Example text to encrypt:  'Buy more Maine potatoes'

Rail fence style:  B   O   A   P   T
                    U M R M I E O A O S
                     Y   E   N   T   E

Read zig-zag:      \  /\  /\  /\  /
                    \/  \/  \/  \/

Encrypted:    BOAPT UMRMI EOAOS YENTE 

"""
# ------------------------------------------------------------------------------
# USER INPUT:

# the string to be en- or decrypted (paste between quotes):
plaintext = """LSSEE EDTEE DTREU COSVR HRVRN RSUDR HSAEF HTEST ROTIA ENTHO EE
"""
# choose wheather to encrypt or decrypt the message:
choice = """decrypt"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ------------------------------------------------------------------------------


def main():
    """Processes the user's choice to en- or decrypt the entered string."""
    if choice == "encrypt":
        print(f"\nMessage to encode: {plaintext}")
        message = process_plaintext(plaintext)
        encrypted_message = encrypt_processed_text(message)
        print(f"Encrypted message: {encrypted_message}.")
    elif choice == "decrypt":
        print(f"\nMessage to decode: {plaintext}")
        message = process_ciphertext(plaintext)
        row_1, row_2, row_3 = split_ciphertext(message)
        decrypted_message = decrypt(row_1, row_2, row_3)
        print(f"Decrypted message: {decrypted_message}.")


def process_plaintext(plaintext):
    """Prepares plaintext for future encryption."""
    processed_text = "".join(plaintext.split()).upper()
    return processed_text


def encrypt_processed_text(message):
    """Encrypts prepared plaintext."""
    top = ""
    middle = ""
    bottom = ""

    for idx, letter in enumerate(message):
        if idx == 0 or idx % 4 == 0:
            top += letter
        elif idx % 2 != 0:
            middle += letter
        else:
            bottom += letter
    combined = top + middle + bottom
    scrambled_text = " ".join([combined[i : i + 5] for i in range(0, len(combined), 5)])
    return scrambled_text


def process_ciphertext(ciphertext):
    """Prepares ciphertext for future decryption."""
    processed_text = "".join(ciphertext.split()).lower()
    return processed_text


def split_ciphertext(message):
    """Splits ciphertext in three rows for decryption."""
    row_2_len = math.ceil(len(message) / 2)
    row_1 = message[: (row_2_len) // 2]
    row_2 = message[(row_2_len) // 2 : row_2_len + (row_2_len) // 2]
    row_3 = message[row_2_len + (row_2_len) // 2 :]
    return row_1, row_2, row_3


def decrypt(row_1, row_2, row_3):
    """Decrypts rows of ciphertext into plain text."""
    plaintext = []
    row_2_part_1 = row_2[::2]
    row_2_part_2 = row_2[1::2]
    for r1, r2, r3, r4 in zip_longest(row_1, row_2_part_1, row_3, row_2_part_2):
        plaintext.append(r1)
        plaintext.append(r2)
        plaintext.append(r3)
        plaintext.append(r4)
    if None in plaintext:
        plaintext.pop()
    return "".join(plaintext)


if __name__ == "__main__":
    main()
