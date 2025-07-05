import random

print("""
      
      Rock-Paper-Scissors Game
      
      Please choose one of them
      
      1 - Rock
      2 - Paper
      3 - Scissors
      4 - Exit Game
      
      Rules:
      1 - Rock beats Scissors
      2 - Scissors beats Paper
      3 - Paper beats Rock
      
      Have fun!
      
      """)

while True:
    User_number = int(input("You choose: "))
    if User_number == 4:
        print("Game over")
        break
    elif (User_number >= 5 or User_number <= 0):
        print("please choose 1-4")
    else:
        Game = {1: "Rock", 2: "Paper", 3: "Scissors"}
        AI_number = random.randint(1,3)
        AI = Game.get(AI_number)
        User = Game.get(User_number)
        print(f"You chose {User}, I chose {AI}")
        if AI_number - User_number == 0:
            print("It is a ")
        elif AI_number - User_number == -1 or AI_number - User_number == 2:
            print("You WIN!")
        else:
            print("You LOST!")
