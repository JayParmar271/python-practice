def numberGuessingGame():
    computerguess = random.randint(1,100)
    myguessnumber = 0
    totalAttempt = 0
    while computerguess != myguessnumber:
        myguessnumber = int(input("enter number\n"))
        if myguessnumber < computerguess:
            print("too low")
        elif myguessnumber > computerguess:
            print("too high")
        totalAttempt += 1

    print("You have given correct answer", myguessnumber)
    print("You have used total attempts", totalAttempt)

numberGuessingGame()
