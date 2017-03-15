spam = ['apples', 'bananas', 'tofu', 'cats', 'elephant', 'dog']
# l = len(spam)
# k = 0
# for i in spam:
#     global k
#     k += 1
#     print(str(k)+' '+i, end=' ')
# for i in range(l+1):
#     print(i)
k = 0
def prinn(argum):
    global k
    for i in argum:
        k += 1
        if k == (len(argum)):
            print('and '+i)
        elif k < (len(argum)-1):
            print(i + ',', end=' ')
        else: print(i, end=' ')

prinn(spam)