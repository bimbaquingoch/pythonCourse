# weigth converter
weigth = int(input("Weigth: "))
unit = input("L(bs) or (K)g: ")

if unit.lower() == "l":
    weigth = weigth * 0.45
    print(f"You are {weigth} kilos")
elif unit.lower() == "k":
    weigth = weigth / 0.45
    print(f"You are {weigth} pounds")
