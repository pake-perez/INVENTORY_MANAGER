# Inventory Manager
# It will let you add, modify or delete items for an inventory

# Needed functions
# Add item
# Update item quantity
# Search specific items
# Sort inventory by: Name, Price, Quantity
# Generate report ?
# Total inventory's value

from functools import reduce

inventory = [{'name': 'tor', 'quantity': 5, 'unit_price': 5.0, 'id': 1}]


def addItem(isRetry):
    name = input("Enter item's name: ")
    quantity = int(input("Enter item's quantity: "))
    unit_price = float(input("Enter item's unit price: "))

    newItem = {'name': name, 'quantity': quantity, 'unit_price': unit_price}
    print('')
    print(newItem)
    isCorrect = input('\nAre the item details correct? Y/N \n')
    if (isCorrect == 'Y'):
        newItem['id'] = len(inventory) + 1
        inventory.append(newItem)
        print('new item added')
    else:
        if (isRetry):
            print('Please try again')
        else:
            addItem(True)


def updateItem():
    sortItems('id', 2)
    shouldPrintInventory = input(
        'Should I print the inventory for you? (Y/N) \n')
    if (shouldPrintInventory == 'Y'):
        print(inventory)

    itemSelected = int(input(
        '\nPlease enter the id of the item you want to update: '))

    item = searchItemBy('id', itemSelected)[0]
    if (item):
        print(item)
        print('Select field to be changed: ')
        keyToBeUpdated = singleCreateCriteriaSelection()
        newValue = input(f'What is the new value for {keyToBeUpdated}? \n')
        inventory[item['id'] - 1][keyToBeUpdated] = newValue
        print('Value updated.')
        print(inventory[item['id'] - 1])
    else:
        print('No item was found with that id \n')


def searchItem():
    print('\nWhich criteria you want to search by?\n')
    searchCriteria = singleCreateCriteriaSelection()
    searchedValue = input(f'What should the value be for {searchCriteria}? \n')
    item = searchItemBy(searchCriteria, searchedValue)
    if (item):
        print(item)
    else:
        print(
            f'No item was found with {searchCriteria} {searchedValue} \n')


def checkTypes(field, item, value):
    currentValue = item[field]
    if (isinstance(currentValue, str)):
        return currentValue == value
    if (isinstance(currentValue, int)):
        return currentValue == int(value)
    if (isinstance(currentValue, float)):
        return currentValue == float(value)


def searchItemBy(field, value):
    return list(filter(lambda item: checkTypes(field, item, value), inventory))


def sortInventory():
    print('\n Which criteria you want to sort by?\n')
    sortCriteria = singleCreateCriteriaSelection()
    direction = int(input(f'''Should the order be 
      1. ascendent 
      2. descendent? \n'''))
    sortItems(sortCriteria, direction)
    print(inventory)


def sortItems(sortCriteria, direction):
    inventory.sort(key=lambda item: item[sortCriteria], reverse=direction == 1)


def singleCreateCriteriaSelection():
    keys = []
    count = 1
    for key in inventory[0].keys():
        print(f"{count}. {key}")
        count += 1
        keys.append(key)
    selectedField = int(input("Enter your choice: "))
    return keys[selectedField - 1]


def multiCreateCriteriaSelection():
    keys = []
    count = 1
    for key in inventory[0].keys():
        print(f"{count}. {key}")
        count += 1
        keys.append(key)
    selection = input("Enter your choices separated by coma (Default all): ")
    fields = []
    if (selection):
        selection = str.split(selection, ',')
        if (len(selection) > 0):
            fields = list(map(lambda num: keys[int(num)-1], selection))
        else:
            print('The selection is not valid \n')
    else:
        fields = list(inventory[0].keys())
    return fields


def filterItemFields(wantedFields, item):
    filteredItem = {}
    for key in item.keys():
        try:
            if (list.index(wantedFields, key) >= 0):
                filteredItem[key] = item[key]
        except ValueError:
            pass
    return filteredItem


def generateReport():
    print('\n Which fields should be reported? \n')
    fields = multiCreateCriteriaSelection()
    if (len(fields) > 0):
        reportedItems = map(
            lambda item: filterItemFields(fields, item), inventory)
        print(list(reportedItems))


def getTotalValue():
    value = 0
    for item in inventory:
        value = value + (item['quantity']*item['unit_price'])
    print(f'Total value of the inventory is: ${value}')


def inventoryMenu():
    while True:
        print('')
        print('----- Welcome to Inventory Manager ------\n')
        print('1. Add new item')
        print('2. Update item')
        print('3. Search item')
        print('4. Sort inventory by name, price or quantity')
        print('5. Generate report')
        print('6. Get total value of the inventory')
        print('7. Exit \n')

        selection = int(input('Please enter your choice: '))
        if (selection == 1):
            addItem(False)
        if (selection == 2):
            updateItem()
        if (selection == 3):
            searchItem()
        if (selection == 4):
            sortInventory()
        if (selection == 5):
            generateReport()
        if (selection == 6):
            getTotalValue()
        if (selection == 7):
            break

    print('Thank you, come back soon!')


inventoryMenu()
