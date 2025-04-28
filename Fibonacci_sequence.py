number1 = 1
number2 = 1
list = [1,1]

for i in range(0,10):
    number = number2
    number2 = number1 + number2
    number1 = number
    list.append(number2)

print(list)