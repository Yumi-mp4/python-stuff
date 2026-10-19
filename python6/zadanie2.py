import random
n = 10
a = 0
b = 10
table = []
while len(table) < n:
    r = random.randint(a,b)
    table.append(r)
print(table)
random.shuffle(table)
print(table)

print("===")

liczby = random.sample(range(a,b), n)
print(liczby)