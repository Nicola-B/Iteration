#Nicola Batty
#14/10/2014
#Iteration class exercises revision

def Task1():
    for count in range(10):
        print("Hello World")

def Task2():
    message = input("please stat a message: ")
    number_of_times = int(input("How many times do you whant it shown: "))
    for count in range(number_of_times):
        print(message)

def Task3():
    total = 0
    avrege_number = int(input("Please enter the number of number needed to avrege: "))
    counter = avrege_number + 1
    for count in range(1,counter):
        number = int(input("Please enter {0} number: ".format(count)))
        total = total + number
    average = total / avrege_number
    print("The average is {0}".format(average))

def Task4():
    number = int(input("Please input a numbe between 10 and 20: "))
    while not(number <= 20 and number >= 10):
        number = int(input("Please input a numbe between 10 and 20: "))
    print("Thank you")

def Task5():
    total = 0
    avrege_number = int(input("Please enter the number of number needed to avrege: "))
    for count in range(avrege_number):
        number = int(input("Please enter {0} number: ".format(count)))
        total = total + number
    total = total - 1
    average = total / avrege_number
    print("The average is {0}".format(average))

def Task6():
    for pounds in range(1,21):
        kilogrames = pounds * 0.453592
        print("{0} pounds : {1}kg".format (pounds, kilogrames)) 