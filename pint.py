pin = str(3216)
att = 0
while att < 3:
    wprowadzony = str(input("podaj pin: "))
    if wprowadzony == pin:
        print("pin poprawny")
        break
    elif wprowadzony != pin:
        print("pin niepoprawny sprobuj ponownie")
        att += 1
if att == 3:
    print("3 proba")