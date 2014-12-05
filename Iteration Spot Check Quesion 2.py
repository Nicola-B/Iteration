#Nicola Batty
#14/11/2014
#Iteration Statement Spot Check Queastion 2

number = int(input("Please enter an integer: "))
times = 1
for count in range(1,13):
    times_table = times * number
    print("{0:>2} * {1} = {2}".format(times, number, times_table))
    times = times + 1
