weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ").lower()
if unit == "l":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit == "k":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("Invalid Input")