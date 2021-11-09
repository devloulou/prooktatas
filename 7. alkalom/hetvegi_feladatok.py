# 1. feladat: az alább megadott listákból hozzátok létre a következő dictionary-t.
# elvárt dictionary: my_dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30 ....}
# 1.2 feladat: az előállított dictionaryből csináljatok egy JSON string objektumot.
# 1.3 feladat: az előállított JSON objektumot írjátok ki egy test.json nevű file-ba.
# A feladatok megoldása során nem elvárás, hogy függvényeket írjatok.
# Azonban ha a feladatokat sikerül megoldani, akkor próbáljátok meg saját
# függvényeket írni, amelyek a feladatokat megoldja, ezzel gyakorolva a függvények fejlesztését.
keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty']
values = [10, 20, 30, 40, None]

my_dict = {}

for idx, item in enumerate(keys):
    my_dict.update({item: values[idx]})

# dict comprehension
my_dict2 = {item: values[idx] for idx, item in enumerate(keys)}

# print(my_dict)
# print(my_dict2)

import json

json_string = json.dumps(my_dict2, indent=4)

#print(json_string)

def json_writer(file_name, data):
    with open(file_name, 'w') as writabele_File:
        json.dump(data, writabele_File)

def json_writer(file_name, data):
    with open(file_name, 'w') as writabele_File:
        json.dump(json.loads(data), writabele_File, indent=4)


#json_writer('hetvegi.json', json_string)




# 2.0 feladat: A csatolt hetvege.txt nevű fileből töröljétek azt a sort / sorokat
# amelyek nem felelnek meg a következő követelményeknek:
# A sorszám és a sor között szükség van egy space-re: valid sor: "Tizedik sor."

def file_line_deleter(file_path):
    data = None
    with open(file_path, 'r+', encoding='utf-8') as file_Object:
        data = file_Object.readlines()
        file_Object.seek(0)
        file_Object.truncate()      
        for item in data:
            if not ' ' in item:
                data.remove(item)
        file_Object.writelines(data)
        
        
           



#file_line_deleter('hetvege.txt')


# 2.1 feladat: ahol hiányzik a pont, oda tegyétek oda a pontot - írjátok bele a file-ba
# Megjegyzés: nem kötelező függvényt írni,
# azonban a legjobb az lenne, ha törekednétek a függvények fejlesztésére

def file_line_deleter(file_path):
    data = None
    with open(file_path, 'r+', encoding='utf-8') as file_Object:
        data = file_Object.read().splitlines()
        print(data)
        file_Object.seek(0)
        file_Object.truncate()
        for idx, item in enumerate(data):
            if not '.' in item:
                item = str(item)+'.\n' if len(data)-1 != idx else str(item)+'.'
            else:
                item = str(item)+'\n'
            file_Object.write(item)


#file_line_deleter('hetvege.txt')



# 3. feladat: Írjatok olyan függvényt, amely tetszőlegesen megadott két számot eloszt.
# Megjegyzés: a feladat megoldása során törekedjetek arra, hogy a matematika szabályai be legyenek tartva:
# pl. 0-val való osztás nem létezik, ha ilyen történne, akkor a program jelezze a felgazsnáló számára, hogy
# 0-ával akart osztani. Ez lehet hibaüzenet, egy kiírás, egy visszatérési érték - bármi.

def devider(a, b):
    eredmeny = False
    try:
        eredmeny = a / b
    except ZeroDivisionError:
        print("Nullával próbáltál meg osztani")
        return False
    except Exception as e:
        print(str(e))

    #return eredmeny

#eredmeny = devider(2,"ricsi")
eredmeny = devider
#print(eredmeny(2,"ricsi"))


# 4. feladat: Írjatok egy olyan függvényt, amely vagy megnyit egy file-t vagy kiír egy file-t,
# annak megfelelően, hogy milyen file nyitás során megadni szükséges módot (w , r, r+, a, a+, w+)
# paraméterben megkapja  a függvény:
# példa függvény meghívására: file_muvelet(file_location, file_mode)

# A példa csak azt szemlélteti, ahogyan meg lehetne hívni az általatok fejlesztett függvényt.
# a paraméterek száma, sorrendje ettől eltérhet.
import os
def file_handler(file_location: str, file_mod:str, data=None):
    check_exist = None
    file_data = None
    if file_mod in ('r'):
        check_exist = os.path.exists(file_location)
        if check_exist:
            with open(file_location, file_mod) as file_Object:
                file_data = file_Object.read()
            return file_data
        else:
            raise Exception(f'A file: {file_location} nem létezik a megadott elérési útvonalon')

    if data and file_mod in ('w'):
        with open(file_location, file_mod) as file_Object:
            file_Object.write(str(data))
        return True
    else:
        raise Exception('Nem adtál meg kiírandó adatot')

file_handler('testecske.txt', 'w', (1))
exit()