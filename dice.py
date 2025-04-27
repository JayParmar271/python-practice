
import random
def dicesGame():
    computerguess = random.randint(1,6)
    myguessnumber = random.randint(1,6)
    # print(computerguess, myguessnumber)

    if myguessnumber < computerguess:
        print("You lose")
    elif myguessnumber > computerguess:
        print("You win")
    else:
        print("Draw")

dicesGame()

