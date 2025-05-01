def login(email, password):
    if email == "k@gmail.com" and password == "k123@45":
        print("You have logged in suceesfully")
    else:
        print("Invalid email or password, Please try again!")

email = input("Enter your email\n")
password = input("Enter your password\n")

login(email, password)
