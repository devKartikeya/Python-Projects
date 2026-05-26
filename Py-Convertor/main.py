import temp_convert
import weight_convert
import binary_convert

if __name__ == "__main__":

    print("Welcome to Py-Convertor !")

    user = input("Press T for Temperature,  W for Weight and B for Binary !").lower()

    if (user == "t"):
        temp_convert.temp_convert()
        
    elif (user == "w"):
        weight_convert.weight_convert()
        
    elif (user == "b"):
        num = int(input("Enter a non-negative integer to convert to binary: "))
        binary_convert.binary_convert(num)