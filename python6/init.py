tuple = (1,7,2,3,8,9,2)

print(tuple)
print(tuple.count(2))
print(tuple.index(2))
if(2 in tuple):
    print("tuple contains 2")

print(len(tuple))
print(max(tuple))
print(sum(tuple))
for x in tuple:
    print(str(x)+",",end='')

print()
#slice
print(tuple[4])
print(tuple[-1])
print(tuple[:3])
print(tuple[-3:])
print(tuple[:-3])
print(tuple[1:4])
print(tuple[1::2])

tuple[1]=4
print(tuple)
