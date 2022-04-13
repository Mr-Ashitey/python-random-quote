from distutils.file_util import write_file
import random


def primary():
    print("Keep it logically awesome.")
    inputQuote = input("Add quote")

    f = open("quotes.txt", "a")
    f.write(inputQuote)
    f.write("\n")
    f.close()

    f = open("quotes.txt", "r")
    quotes = f.readlines()
    f.close()
    # print(quotes)

    # last = len(quotes) - 1
    # rnd = random.randint(0, last)

    for quote in quotes:
        print(quote.rstrip())


if __name__ == "__main__":
    primary()
