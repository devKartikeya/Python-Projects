import random

print("Welcome to Rock Paper Scissors Game")
print("Press R for Rock, P for Paper and S for Scissors")

choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
winning_pairs = {("S", "P"), ("P", "R"), ("R", "S")}

computer = random.choice(list(choices.keys()))
user = input("Enter your Choice: ").upper()

if user not in choices:
    print("Invalid choice! Please select R, P, or S.")
else:
    print(f"Computer chose {choices[computer]}")

    if user == computer:
        print("Match is Drawn!")
    elif (user, computer) in winning_pairs:
        print("You Won!")
    else:
        print("You Lose!")
