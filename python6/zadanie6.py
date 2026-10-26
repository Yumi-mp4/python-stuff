zdanie = "Always look on the bright side of life"
n = 3

wynik = []

for i in range(0, len(zdanie), n):
    wynik.append(zdanie[i:i+n])

print(wynik)

# pomijanie spacji

zdanie = "Always look on the bright side of life"
n = 3
zdanie = zdanie.replace(" ","")

wynik = []

for i in range(0, len(zdanie), n):
    wynik.append(zdanie[i:i+n])

print(wynik)