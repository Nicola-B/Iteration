#Nicola Batty
#06/11/2014
#Iteration Class exercises strech and challenge

def Task1():
    number = int(input("Pelease input a number: "))
    number_times = number + 1
    intiger = 1
    for count in range(1, number_times,5):
        number1 = number ** intiger
        intiger = intiger + 1
        number2 = number ** intiger
        intiger = intiger + 1
        number3 = number ** intiger
        intiger = intiger + 1
        number4 = number ** intiger
        intiger = intiger + 1
        number5 = number ** intiger
        print("{0:}|{1:}|{2:}|{3:}|{4:}".format(number1, number2, number3, number4, number5))
        intiger = intiger + 1
