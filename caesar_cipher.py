print("ceasar cipher shifter")

word = "helloworld!"
shifted_word = ""
shift = 27
shift = shift % 26

for letters in word:
    shifted = ord(letters) + shift
    if shifted > 122:
        shifted -= 26
        shifted_word += chr(shifted)
    elif letters.isalpha():
        shifted_word += chr(shifted)
    else:
        shifted -= shift
        shifted_word += chr(shifted)

print(shifted_word)
