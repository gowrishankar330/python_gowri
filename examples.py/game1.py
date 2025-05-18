import random
options = ["rock", "paper", "scissor"]
running = True
while running:
    jury = random.choice(options)
    player = None
    while player not in options:
      player = input(f"Enter an option (rock, paper, scissor): ")
    print(f"jury: {jury}")
    print(f"player: {player}")
    if player == jury:
        print("it's a tie mamae!")
    elif player == "rock" and jury=="scissor":
        print("you win")
    elif player =="paper" and jury=="rock":
        print("you win")
    elif player == "scissors" and jury == "paper":
        print("you win")
    else:
        print("you lose")
    tryagain = input("you wanna play again(y or n): ")
    if tryagain == "n":
     running = False
print("thanks for playing")

