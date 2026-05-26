import random

#Welcome Message
print("Welcome to the Number Guess Game !")

#Generating Random Number
def generateRandom():
    rand = random.randint(1,101)
    return rand

#Main Function
def main():
    rand = generateRandom()
    print("Number has been Generated !")
    
    #Loop to check Rounds
    for i in range(1,11): 
        
        if (i == 10):
            print("Sorry, Limit Reached !\n It was ", rand)
            break
        
        user = int(input("Enter your Guess ! : "))
    
        #Winning Check of Match
        if (user == rand):
            print("WoW, You guessed it right !\nIt was ", rand)
            print("Number of attempts: ", i)
            break
        
        elif(user < rand):
            print("Too Small, Guess Higher !")
        
        elif(user > rand):
            print("Too Large, Guess Lower !")
    
    
main()