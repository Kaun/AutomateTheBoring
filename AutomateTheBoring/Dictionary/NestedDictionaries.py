allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwitches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
     numBrought = 0
     for k, v in guests.items():
         numBrought += v.get(item, 0)
#         # print(k, v)
     return numBrought

print('- Apples: ' + str(totalBrought(allGuests, 'apples')))

