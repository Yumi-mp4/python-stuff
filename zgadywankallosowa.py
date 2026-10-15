import random
cel = random.randint(1,50)
guess = 0
att = 1
print(cel)

while guess != cel:
    guess = int(input("Podaj liczbe: "))
    if guess > cel:
        print("cel mniejszy")
        att += 1
    elif guess < cel:
        print("cel wiekszy")
        att += 1

print("wygrales za " + str(att) + " podejsciem")    