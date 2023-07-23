import sys


def open_file(file):
    try:
        with open(file, "r") as file:
            all_words = (word.strip() for word in file.readlines())
            return set(all_words)

    except IOError as e:
        print(e)
        sys.exit()
