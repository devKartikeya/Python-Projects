import random

print("Welcome to Rock Paper Scissors Game")
print("Press R for Rock, P for Paper and S for Scissors")

choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
winning_pairs = {("S", "P"), ("P", "R"), ("R", "S")}

user_count = 0
computer_count = 0

for i in range(1,11):

    computer = random.choice(list(choices.keys()))
    user = input("Enter your Choice: ").upper()

    if (i == 10):
      if (user_count > computer_count):
          print("You Won the Match , Champion !")
          print("Your Score: ", user_count)
          break
      else:
          print("You lose the Match, Better Luck next Time !")
          print("Your Score: ", user_count)
          break
        
    if user not in choices:
        print("Invalid choice! Please select R, P, or S.")
    else:
        print(f"Computer chose {choices[computer]}")

    if user == computer:
        print("Match is Drawn!")
    elif (user, computer) in winning_pairs:
        print("You Won!")
        user_count = user_count + 1
    else:
        print("You Lose!")
        computer_count = computer_count + 1
