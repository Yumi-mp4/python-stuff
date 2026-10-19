sentence = "Always look on the bright side of life"
lista = []

print(sentence.upper())
print(sentence.title())
print(sentence.index("look")+1)
print(sentence.isascii())
print(sentence.replace(" ","..."))
lista.append(sentence.split(" "))
print(lista)
print(sentence[1:-1])
print(sentence.replace(sentence, "Always look on the bright side of your life"))