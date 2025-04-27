investedamount=int(input("give me a amount\n"))
intrestrate=int(input("give me a rate\n"))
totalyear=int(input("give me a year\n"))
totalmaturityamount=investedamount

for number in range(0,totalyear):
    interest=(totalmaturityamount *intrestrate)/100
    totalmaturityamount += interest
    totalinterest = totalmaturityamount-investedamount

print(f"Your total interest is {totalinterest}, Maturity amount: {totalmaturityamount}")