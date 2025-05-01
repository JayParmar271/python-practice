def login(email,password):
    if email == "k@gmail.com" and password =="k123@45":
        print("You have logedin suceesfully")
    else:
        print("invalid email and password")

email = input("Enter your email\n")
password = input("Enter your passwoed\n")

login(email,password)
