# Inventory Manager

This is a project to simulate the inventory management of an enterprise

## Usage

Start the program by running the file reto_inventario.py

You will be promped with 7 options

```
----- Welcome to Inventory Manager ------

1. Add new item
2. Update item
3. Search item
4. Sort inventory
5. Generate report
6. Get total value of the inventory
7. Exit

Please enter your choice:
```

### 1. Adding new Item

When you select the number 1 option on the main menu, you can add a new item

```
Please enter your choice: 1
Enter item's name: Screws
Enter item's quantity: 4
Enter item's unit price: 10

{'name': 'Screws', 'quantity': 4, 'unit_price': 10.0}

Are the item details correct? Y/N
```

If you accidentally input something wrong you can hit 'N' and it will let you try to enter your data once again, otherwise it will insert the new item and return to the main menu:

```
Are the item details correct? Y/N
Y
new item added
```

Note: If you unsuccessfully enter your data on the second change, the operation will be aborted.

### 2. Update item

You are able to modify an item's data, when you select number 2, you can print the whole inventory if you want, so you can check which item to modify, pay attention to the id of the item you want to modify:

```
Should I print the inventory for you? (Y/N)
Y
[{'name': 'tor', 'quantity': 5, 'unit_price': 5.0, 'id': 1}, {'name': 'Screws ', 'quantity': 4, 'unit_price': 10.0, 'id': 2}]

Please enter the id of the item you want to update:
```

Once the id is selected, you will now be prompted to select which field you want to update:

```
Please enter the id of the item you want to update: 2
{'name': 'Screws ', 'quantity': 4, 'unit_price': 10.0, 'id': 2}
Select field to be changed:
1. name
2. quantity
3. unit_price
4. id
Enter your choice:
```

For this example we picked name field:

```
Enter your choice: 1
What is the new value for name?
Bolts
Value updated.
{'name': 'Bolts', 'quantity': 4, 'unit_price': 10.0, 'id': 2}
```

Now the information has been updated on the inventory.

### 3. Search item

With this option you are able to search for any item matching the value you entered:

```
Please enter your choice: 3

 Which criteria you want to search by?

1. name
2. quantity
3. unit_price
4. id
Enter your choice: 1
What should the value be for name?
Bolts
[{'name': 'Bolts', 'quantity': 4, 'unit_price': 10.0, 'id': 2}]
```

### 4. Sort Inventory

With this option you are able to sort the inventory and retrieve it sorted.

```
Please enter your choice: 4

Which criteria you want to sort by?

1. name
2. quantity
3. unit_price
4. id
Enter your choice: 1
Should the order be
      1. ascendent
      2. descendent?
2
[{'name': 'Bolts', 'quantity': 4, 'unit_price': 10.0, 'id': 2}, {'name': 'tor', 'quantity': 5, 'unit_price': 5.0, 'id': 1}]
```

### 5. Generate Report

You can retrieve the inventory, filtering which fields you want to be shown, this is following the same approach as for the others actions:

```
Please enter your choice: 5

Which fields should be reported?

1. name
2. quantity
3. unit_price
4. id
Enter your choices separated by coma (Default all): 4,1,2
[{'name': 'Bolts', 'quantity': 4, 'id': 2}, {'name': 'Bolts', 'quantity': 3, 'id': 3}, {'name': 'tor', 'quantity': 5, 'id': 1}]
```

Note: You can leave the selection empty if you want to retrieve all fields

### 6. Generate Report

This will print you the total value of the inventory you currently have

```
Please enter your choice: 6
Total value of the inventory is: $92.0
```

### 7. Exit

You will just exit the inventory manager program

## License

[MIT](https://choosealicense.com/licenses/mit/)
