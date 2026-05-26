import random
import string

print("Welcome to PyProPassGen !")

alpha_list   = list(string.ascii_letters)
digit_list = list(string.digits)

length = int(input("Enter the Length of the Password :" ))

is_digit = input("Press Y to include Digits in Password and Press N for Not : ").lower()

password = ""

random.shuffle(alpha_list)
random.shuffle(digit_list)

if (is_digit == "y"):
    alpha_list.extend(digit_list)
    random.shuffle(alpha_list)

for i in range (length):
    password += random.choice(alpha_list)
    
print("Your Password is : " + password)