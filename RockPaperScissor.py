import random
print("Computer's Turn: Rock(r), Paper(p) or Scissor(s)?")
computer=''
    
    
def gamewin(computer, player):
    if computer == 'r':
        if player == 'p':
            return True
        elif player == 's':
            return False
        
    elif computer == 'p':
        if player == 's':
            return True
        elif player == 'r':
            return False 
        
    elif computer == 's':
        if player == 'r':
            return True
        elif player == 'p':
            return False
        

randomNumber = random.randint(1, 3)

if randomNumber == 1:
    computer = 'r'
    
elif randomNumber == 2:
    computer = 'p'
    
elif randomNumber == 3:
    computer = 's'

i = 1
while i <= 3:
    player = input("Your's Turn: Rock(r), Paper(p) or Scissor(s)?")
    game = gamewin(computer, player)
    # i += 1

    print(f"Computer choose {computer}")
    print(f"Player choose {player}")

    if game == None:
        print("The game is Draw")
            
    elif game:
        print("You Win!")
            
    else:
        print("Computer Win !")
    i+=1