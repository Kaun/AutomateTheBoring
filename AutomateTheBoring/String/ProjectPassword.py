#! python3
import sys
import pyperclip

psw = {'email': 'whatyouremail',
            'job': '525672',
            'bank': '777', }
# while True:

if len(sys.argv) < 2:
    print('Usage: python password.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]
# arg = input('Enter password what you want: ')
if account in psw:
    print(account, psw[account])
    pyperclip.copy(psw[account])
    print('Success')
else:
    print('Not password. Enter Z to exit')



