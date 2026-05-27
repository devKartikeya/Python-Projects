
if __name__ == "__main__":

    print("Welcome to the Pythonic To-Do-List")
    user = input("Press S for Displaying all To-Dos and Press N for adding a New Todo! ").lower()

    def display_todos():
        with open('./To-Do-List/To-Dos.txt', 'r') as file:
            lines = file.readlines()
    
        print("\nYour To-Do List:")
        for index, todo in enumerate(lines, start=1):
            print(f"{index}. {todo.strip()}")


    if user == 's':
        display_todos()

    elif user == 'n':
        todo = input("Enter your To-Do! ")
        with open('./To-Do-List/To-Dos.txt', 'a') as file:
            file.write(f"{todo}\n")
        print("Done")
        
        display_todos()
    
    
