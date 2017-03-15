# spam = ['a','b','c','d']
# bacon = [3.14, 'cat', 11, 'cat', True]
# bacon.append(99)
# bacon.remove('cat')
# print(bacon)
# print(spam)
# all = list()
# all += spam*2
# all.remove('c')
# print(all)

string = 'мама мыла раму'
massiv = list(string)
# print(massiv)
massiv_copy = massiv[:]
# print(massiv_copy)
def dell(mas, arg):
    new_mas = list()
    for i in mas:
        if i != arg:
            new_mas += i
    return print(new_mas)

dell(massiv_copy, 'м')
print(massiv)