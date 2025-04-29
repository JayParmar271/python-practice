name =input("what is your name?\n")[::-1]
print(name)

number=input("give me a number?\n")
reversnumber = number[::-1]
print(reversnumber)

if number==reversnumber:
    print("this is palindrome number\n")
else:
    print("this is not palindrome number\n")
