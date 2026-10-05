pierwsza = 220
druga = 284
temp = 1
sumapierw = 0
sumadru = 0

for i5 in range(pierwsza):
    if pierwsza % temp == 0:
        print(temp)
        sumapierw += temp
    temp = temp + 1

print("=========")
temp = 1

for i in range(druga):
    if druga % temp == 0:
        print(temp)
        sumadru += temp
    temp += 1

print("========")
# print(f"{sumapierw} and {sumadru}")
if sumadru == sumapierw and sumapierw == sumadru:
    print("sa zaprzyjaznione")
    print(f"{sumadru}, {sumapierw}")
else:
    print("nie sa")
    print(f"{sumadru}, {sumapierw}")