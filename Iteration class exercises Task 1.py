#Nicola Batty
#14/10/2014
#program to prompt for 8 numbers and report the total to the user

print("Hello Uesr")

total = 0

for count in range(1,9):
    number = int(input('Enter number {0} : '.format(count)))
    total = total + number
print('The total is {0}'.format(total))

