birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
trueAnswer = ['Y', 'y']
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name])
    else:
        print('I don\'t have birthday information of' + name)
        print('Do you have enter new birthday of user:'+name)
        print('Y - yes, N - no')
        answer = input()
        if answer in trueAnswer:
            print('Enter birthday')
            bDay = input()
            birthdays[name] = bDay
            print('Database update')
        else:
            print('Good bay')
            break