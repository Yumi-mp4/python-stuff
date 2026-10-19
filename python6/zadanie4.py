sentence = "Always look on the bright side of life"
vow = []
for letter in sentence.lower():
    if letter in "aeiou":
        vow.append(letter)
print(vow)