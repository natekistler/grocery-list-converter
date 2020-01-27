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
count = 1
for item in grocery_list_df['List_Item']:
    try:
        i = grocery_store_inventory.loc[grocery_store_inventory['Item'] == item]
        location_dic[grocery_store_inventory['Location'][i.index[0]]].append(item)
        print('Added', item, ':',  count, 'of', len_list, 'to shopping list')
        count += 1
    except (ValueError, IndexError):
        location_dic['other'].append(item)
        print('Added', item, ":", count, 'of', len_list, 'to shopping list')
        count += 1

print(location_dic)