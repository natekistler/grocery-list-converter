import pandas as pd

grocery_store_inventory = pd.read_excel('grocery-store-items.xlsx')

def unique(lis):
    unique_list = []
    for i in lis:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

#Make all items and locations in grocey_store_inventory lowercase to ease string comparison
for cols in grocery_store_inventory.columns:
    try:
        grocery_store_inventory[cols] = grocery_store_inventory[cols].str.lower()
    except:
        pass

grocery_list = ['Milk', 'Eggs', 'Apples', 'Strawberries']
grocery_list_df = pd.DataFrame(grocery_list, columns=['List_Item'])
grocery_list_df['List_Item'] = grocery_list_df['List_Item'].str.lower()

locations_list = unique(grocery_store_inventory['Location'])

location_dic = {}

for location in locations_list:
    location_dic.update({location: []})

location_dic.update({'other': []})

len_list = len(grocery_list)

for grocery_item in grocery_list_df['List_Item']:
    inventory_index = 0
    ind_item_loc = []
    for inventory_item in grocery_store_inventory['Item']:
        if grocery_item in inventory_item:
            location = grocery_store_inventory['Location'][inventory_index]
            ind_item_loc.append(location)
        inventory_index += 1
    try:
        if len(ind_item_loc) == 0:
            print('Found no matches for ' + grocery_item + '. Please choose a location or other.')
            location_choice = input('Location choice: ')
            location_dic[location_choice].append(grocery_item)
        elif len(ind_item_loc) > 1:
            print('Found multiple locations for ' + grocery_item + '. Choose one: ' + str(ind_item_loc) + '.')
            location_choice = input('Location choice: ')
            location_dic[location_choice].append(grocery_item)
        else:
            location_dic[location].append(grocery_item)
    except KeyError:
        pass

print(location_dic)