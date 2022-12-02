number = input('Entera number:')

try:
    print(int(number) * 2)
except ValueError:
    print("You did not enter a base 10 number! try again.")