def temp_convert():
    
    user = input("Press C for Celsius , K for Kelvin and F for Fahrenheit for Temperature!").lower()

    if (user == "c"):
        temp = int(input("Enter Temperature in Celsius !"))
        result = celsiusConversion(temp)
        print(f"The Temperature in Fahrenheit is {result[0]} and in Kelvin is {result[1]}")
    
    if (user == "k"):
        temp = int(input("Enter Temperature in Kelvin !"))
        result = fahrenheitConversion(temp)
        print(f"The Temperature in Celsius is {result[0]} and in Fahrenheit is {result[1]}")

    if (user == "f"):
        temp = int(input("Enter Temperature in Fahrenheit !"))
        result = kelvinConversion(temp)
        print(f"The Temperature in Celsius is {result[0]} and in Kelvin is {result[1]}")

    

def celsiusConversion(temp):
    fahrenheit = ( (temp * 9)/ 5 ) + 32
    kelvin = temp + 273.15
    return [fahrenheit, kelvin]

def fahrenheitConversion(temp):
    celsius = ( temp - 32 ) *  5 / 9
    kelvin = ( temp - 32 ) *  5 / 9 + 273.15
    return [celsius, kelvin]

def kelvinConversion(temp):
    celsius = temp - 273.15
    fahrenheit = ( temp - 273.15 ) * 9 / 5  + 32
    return [celsius, fahrenheit]