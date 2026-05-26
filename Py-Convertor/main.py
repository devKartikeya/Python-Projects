import temp_convert
import weight_convert

if __name__ == "__main__":

    print("Welcome to Py-Convertor !")

    user = input("Press T for Temperature and W for Weight !").lower()

    if (user == "t"):
        temp_convert.temp_convert()
        
    elif (user == "w"):
        weight_convert.weight_convert()