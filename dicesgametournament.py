import random

def dicesGameTournament():
    computerwon = 0
    userwon = 0

    for i in range(0,5):
        computerdice = random.randint(1, 6)
        userdice = random.randint(1, 6)

        if computerdice < userdice:
            print("You lose")
            computerwon += 1
        elif computerdice > userdice:
            userwon += 1
            print("You win")
        else:
            print("Draw")

    print(computerwon, userwon)

    if computerwon < userwon:
        print("Finally you win")
    elif computerwon > userwon:
        print("Finally you lose")
    else:
        print("Finally draw")

dicesGameTournament()
