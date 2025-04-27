sum=0
totalnumber=int(input("give me a number\n"))
for number in range(0,totalnumber):
    number=int(input("enter number\n"))
    sum=sum+number
average=sum/totalnumber
print(average)