invent = {'rope': 1, 'torch': 6, 'gold coin': 42,
          'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'rope']

def displayInventory(dict):
    print('Inventory:')
    item_total = 0
    for k, v in dict.items():
        print(k, v)
        item_total += v
    return print('Total:', item_total)

def addToInvertory(inventory, addedItems):
    dictItems = {}
    newDict = {}

#Считаем количество элементов в списке и создаем словарь
    for i in addedItems:
        dictItems.setdefault(i, 0)
        dictItems[i] += 1

# Сравниваем ключи в двух словарях,
# при совпадении складываем значения и объединяем словари
    for i, k in inventory.items():
        for l, m in dictItems.items():
            if i == l:
                newDict[i] = k + m
            # else:
            #     newDict[i] = k
    inventory.update(newDict)
#    print('Items dragon', dictItems)
#    print('New dict', inventory)


sorted(invent)
print('Invent', invent)
addToInvertory(invent, dragonLoot)
print('New Invent:', invent)

displayInventory(invent)

