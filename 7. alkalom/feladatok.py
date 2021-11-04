# 1. feladat: Listázzuk ki a megadott dictionary-ból az autók típusait.
#pl: my_list = ['Mercedes', 'Volvo', 'BMW']
# 1.2 feladat: Listázzuk az összes kulcs értéket a megadott dictionaryből
# 1.3 feladat: Listázzuk az összes olyan auto-t, amelynek a motorja 1.4-esnél nagyobb.

my_dict = {
    'prev_year': {
        'auto': [
    {
        'color': "Purple",
        'motor': 1.6,
        'gas_type': "benzin",
        'type': "Mercedes"               
    },
    {
        'color': "Yellow",
        'motor': 1.1,
        'gas_type': "diesel",
        'type': "Seat"               
    },
    {
        'color': "Black",
        'motor': 1.9,
        'gas_type': "benzin",
        'type': "BMW"               
    }
    ]},
     
    'act_year': {
        'auto': [
    {
        'color': "Gold",
        'motor': 1.6,
        'gas_type': "benzin",
        'type': "Volvo"               
    },
    {
        'color': "Blue",
        'motor': 1.4,
        'gas_type': "diesel",
        'type': "Renault"               
    },
    {
        'color': "Orange",
        'motor': 2.2,
        'gas_type': "benzin",
        'type': "Toyota"               
    }]

    }
}

#Listázzuk ki a megadott dictionary-ból az autók típusait.
#pl: my_list = ['Mercedes', 'Volvo', 'BMW']

my_list = []

print(my_dict['prev_year']['auto'][0]['motor'])
print(my_dict['act_year']['auto'][0]['motor'])
print(type(my_dict['prev_year']['auto'][0]['motor']))

##### 
## 'prev_year' -> key
## my_dict['prev_year'] -> value

for key, value in my_dict.items():
    for item in value['auto']:
        if item['motor'] > 1.4:
            my_list.append(item['type'])

print(my_list)
exit()

for key, value in my_dict.items():
    for item in value['auto']:
        my_list.append(item['type'])

#print(my_list)

my_list = []
my_list2 = []

for key, value in my_dict.items():
    my_list.append(key)
    for k, v in value.items():
        my_list.append(k)
        for item in v:
            my_list.extend(item.keys())


my_list2.extend(my_dict.keys())
my_list2.extend(my_dict['prev_year'].keys())
my_list2.extend(my_dict['act_year'].keys())
my_list2.extend(my_dict['prev_year']['auto'][0].keys())
my_list2.extend(my_dict['prev_year']['auto'][1].keys())
my_list2.extend(my_dict['prev_year']['auto'][2].keys())
my_list2.extend(my_dict['act_year']['auto'][0].keys())
my_list2.extend(my_dict['act_year']['auto'][1].keys())
my_list2.extend(my_dict['act_year']['auto'][2].keys())

print(my_list)
print(my_list2)

my_list = []

for key, value in my_dict.items():
    for item in value['auto']:
        my_list.append(item['type'])

