def weight_convert():
    print("Welcome to Weight Convertor !")

    user = input("Press K for Kilograms and P for Pounds !").lower()

    if (user == "k"):
        kg = float(input("Enter the weight in Kilograms : "))
        print(f"{kg} Kilograms is equal to {kg * 2.20462} Pounds !")

    elif (user == "p"):
        lb = float(input("Enter the weight in Pounds : "))
        print(f"{lb} Pounds is equal to {lb * 0.453592} Kilograms !")

    else:
        print("Invalid Input !")