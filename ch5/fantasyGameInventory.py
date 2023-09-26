# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    # your code goes here
    addedItemsDict = {}
    for index, item in enumerate(addedItems):
        addedItemsDict.setdefault(item, 0)
        addedItemsDict[item] += 1

    for k, v in addedItemsDict.items():
        if (inventory.get(k, 0) == 0): inventory[k] = v
        else: inventory[k] += v

    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
