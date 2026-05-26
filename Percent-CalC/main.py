print("Welcome to Percent-Calc !")

def percent_calc():
    length = int(input("Enter the numnber of subjects !"))
    
    total_marks = 0
    for i in range(length):
        marks = int(input(f"Enter the marks for subject {i+1} !"))
        total_marks += marks
    percentage = (total_marks / (length * 100)) * 100
    print(f"The percentage is {percentage} %")
    
if __name__ == "__main__":
    percent_calc()