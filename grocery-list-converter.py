import pandas as pd

grocery_store_inventory = pd.read_excel('grocery-store-items.xlsx')

grocery_list = []

for item in grocery_store_inventory['Item']:
    print(item)