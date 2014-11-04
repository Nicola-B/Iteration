#Nicola Batty
#27/10/2014
#Iteration Class exersises development

def Task1():
    n = -1
    total = 1
    while n < 0:
        n = int(input("Input a number: "))
        n = n+1
    for count in range(1,n):
        total = total * count
    print("the total is {0}".format(total))

def Task2():
    stars = int(input("Please input the number of stars: "))
    rows = int(input("Please input the number of rows: "))
    for count in range(rows):
        print("*" * stars)

def Task3():
    numbers = input("Please input the one diget numbers: ")
    for count in numbers:
        print (count)

def Task4():
    number_serease = int(input("Please input number of numbers in serease: "))
    number1 = int(input("Please input a number: "))
    for count in range(2,number_serease):
        number = int(input("Please input a number: "))
        if number > number1:
            number1 = number 
        else:
            number1 = number1
    number = int(input("Please input a negative number: "))
    if number > number1:
        number1 = number 
    else:
        number1 = number1
    print ("The bigest number is {0}".format(number1))
