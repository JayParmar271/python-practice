def calculator(number1, number2, operation):
    if operation == "+":
        print(f"Result : {number1 + number2}")
    elif operation == "-":
        print(f"Result : {number1 - number2}")
    elif operation == "*":
        print(f"Result : {number1 * number2}")
    elif operation == "/":
        print(f"Result : {number1 / number2}")
    else:
        print("Given operation is invalid, Please use +, -, *, /")

number1 = int(input("Give me a number1\n"))
number2 = int(input("Give me a number2\n"))
operation = input("Give me a operation\n")

calculator(number1, number2, operation)