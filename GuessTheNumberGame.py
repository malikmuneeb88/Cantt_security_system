import random

randomNumber = random.randint(1, 50)

userGuess = None

Guesses = 0

while(userGuess != randomNumber):
    userGuess = int(input("Enter a number u guess:\n"))
    Guesses += 1
    
    if(userGuess == randomNumber):
        print("You Guessed it right!!")
        
    else:
        if(userGuess > randomNumber):
            print("You Guessed it wrong! Enter Smaller number: \n")
        else:
            print("You Guessed it wrong! Enter larger number: \n")
            
print(f"You guessed the number in {Guesses} guesses")