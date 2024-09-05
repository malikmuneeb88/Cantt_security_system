import random

while True:
    
    print("\n")
    
    print("1) Rock.\n")
    print("2) Paper.\n")
    print("3) Scissors.\n")
    
    choice = int(input("Enter Choice: "))
    
    if(choice == 1):
        player = "Rock"
        
    elif(choice == 2):
        player = "paper"
        
    elif(choice == 3):
        player = "Scissors"
        
    print("\n")
    
    print("player choose", choice )
    
    Throws = ["Rock", "Paper", "Scissors"]
    computer = random.choice(Throws)
    
    print("computer choose", computer)
    
    if(player == computer):
        print("Tie Game !")
        
    elif(player == "Rock"):
        if(computer == "Paper"):
            print("Computer wins !")
        elif(computer == "Scissors"):
            print("Player wins !")
            
    elif(player == "Paper"):
        if(computer == "Rock"):
            print("Player wins !")
        elif(computer == "Scissors"):
            print("Computer Wins !")
    
    elif(player == "Scissors"):
        if(computer == "Rock"):
            print("Compute Wins !")
        elif(computer == "Paper"):
            print("Player Wins ")
            
    print("\n")
    
    print("1) Play Again.\n")
    print("2) Quit.\n")
     
    choice = int(input("Enter Your choice:\n"))
    
    
    if(choice == 2):
        break