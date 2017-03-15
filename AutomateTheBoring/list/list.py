catStr = 'a b c d e f'
catList = catStr.split(' ')
catNames = list()
while True:
    print("Input the name of cat " + str(len(catNames)+1))
    name = input()
    if name == '':
        break
    else:
        # catNames.append(name)
        catNames += name
print(catNames)
for i in catNames:
    print(i, end=' ')
print()
print(catList)
for n in catList:
    print(n, end=' ')
