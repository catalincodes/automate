def collatz(number):
    if (number % 2 == 0):
        return number / 2
    else:
        return 3 * number + 1

print('Enter number:')
originalNumber = int(input())
number = originalNumber

while (number != 1):
    number = int(collatz(number))
    print(number)
