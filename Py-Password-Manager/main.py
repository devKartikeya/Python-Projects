import os 
print('Welcome to the Python Password Manager !')

def add_password(password, key, dir):
    with open(dir, "a") as f:
        out = f.write(f"{key} => {password} \n")
        if out: 
            print('Password Inserted ', out)
            
def get_passwords(dir):
    f = open(dir, "r")
    admin = f.readline().strip()
    admin_password = input("Enter Admin Password: ").strip()
    if (admin_password == admin):
        with open(dir, "r") as f:
            for password in f.readlines():
                print(password)
    else:
        print('Invalid Credentials !')   
def main():
    user = input("Enter 'A' to Add Password and 'G' to Get all Passwords: ").lower()
    dir = os.path.join(f"{os.getcwd()}\\", "Py-Password-Manager\\passwords.env")
    if user == 'a': 
        password = input('Enter your Password: ')
        key = input('Enter your Key: ')
        add_password(password, key, dir)
        
    elif user == 'g':
        get_passwords(dir)
        
    else: 
        print('Please enter a valid option !')

main()