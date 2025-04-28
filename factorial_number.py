#.......... Factorial number:
# 5 * 4 * 3 * 2 * 1 = 120
#
# 7 * 6 * 5 * 4 * 3 * 2 * 1 = 5040......... :

#5*4*3*2*1=answer
number = int(input("Give me number?"))
fact = 1

while number > 0:
    fact *= number
    number -= 1
    
print(fact)