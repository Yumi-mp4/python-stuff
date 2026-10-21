sentence = "Always look on the bright side of life"

# print(ord("A"))

for i in range(len(sentence)):
    letter = sentence[i]
    if letter in "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz":
        print(f"{letter}  ASCII:  {ord(letter)}")