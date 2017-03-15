
def collatz(number):
    i =0
    maxNum = number
    while number != 1:
        if number % 2 == 0:
            number /= 2
            if number > maxNum:
                maxNum = number
            i += 1
            print(int(number))
        elif number % 2 == 1:
            number = number*3+1
            print(int(number))
            i += 1
            if number > maxNum:
                maxNum = number

    return print('Count:',i,'Max number:', int(maxNum))
#collatz(27)
print('Enter number and show Collatz Sequence')
try:
    num = int(input())
    collatz(num)
except ValueError: print('Not correct data')