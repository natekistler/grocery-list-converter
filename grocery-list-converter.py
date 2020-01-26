import pandas as pd

grocery_store_inventory = pd.read_excel('grocery-store-items.xlsx')

for cols in grocery_store_inventory.columns:
    try:
        grocery_store_inventory[cols] = grocery_store_inventory[cols].str.lower()
    except:
        pass

grocery_list = []

for item in grocery_list:
    for inventory in grocery_store_inventory['list']:
        print(item)