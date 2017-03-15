while True:
    age = input('Enter age ')
    if age.isdecimal():
        print('Correct input:', age)
        break
while True:
    pasw = input('Enter password ')
    if pasw.isalnum():
        print('Correct input password')
        break
    else: print('Only num and alph')
