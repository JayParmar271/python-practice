def isPrimeNumber(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = int(input("Give me a number \n"))
isPrime = isPrimeNumber(number)
if (isPrime):
    print("This is prime number", number)
else:
    print("This is not prime number", number)