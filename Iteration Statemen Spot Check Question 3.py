#Nicola Batty
#14/11/2014
#Iteration Statemen Spot Check Question 3

guessed = "fulse"
number = 94
turns = 0
while guessed == "fulse":
    turns = turns + 1 
    user_guess = int(input("Enter your guess for the number: "))
    if user_guess == number:
        guessed = "true"
    elif user_guess > number:
        print("The number you guessed is too high")
    else:
        print("The number you guessed is too low")
print("you took {0} turns o guess the number".format(turns))
print("The number was: {0}".format(number))
