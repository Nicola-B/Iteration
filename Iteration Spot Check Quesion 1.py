#Nicola Batty
#1/11/2014
#Ieration Spot Check Quesion 1

number = 0
total = 0
while number > -1:
    number = int(input("Please enter a number: "))
    total = total + (number*number)
total = total - (number*number)
print("The total is {0}".format(total))
