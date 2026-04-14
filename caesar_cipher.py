import re

word = "hello"
number = 1
if number > 25:
    shift = number - 26
else:
    shift = number


def ceaser_shift(letter):
    capital_letter = r"[A-Z]"
    try:
        if re.match(capital_letter, letter):
            shifted = (ord(letter) + 32) + shift
        else:
            shifted = ord(letter) + shift

        if shifted > 122:
            corrected = shifted - shift - 25
            return chr(corrected)
        else:
            return chr(shifted)

    except TypeError:
        print("invalid characters!, skipping")


def cshift():
    try:
        result = ""
        for letter in word:
            result += ceaser_shift(letter)

        print(word, "is shifted by", number, "becomes",result)

    except TypeError:
        print("invalid settings!")

cshift()

