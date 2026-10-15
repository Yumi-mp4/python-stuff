dana = 1
dzielniki = []

for i in range(1, dana):
    if dana % i == 0:
        dzielniki.append(i)
print("--------")
print("dzielniki: " + (str(dzielniki)))
print("suma: " + str(sum(dzielniki)))

if sum(dzielniki) == dana:
    print(True)
else:
    print(False)