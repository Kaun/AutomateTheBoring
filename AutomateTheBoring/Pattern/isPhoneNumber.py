def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def seachNumber(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if isPhoneNumber(chunk):
            print(chunk)


massage = 'sdds 432-344-3442 is a phone number: 422-344-3442'
seachNumber(massage)

# print('432-344-3442 is a phone number:')
# print(isPhoneNumber('432-344-3442'))

