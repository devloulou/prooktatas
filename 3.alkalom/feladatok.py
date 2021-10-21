# 1. feladat: a megadott lista tartalmaz ismétlődő értékeket. 
# Hozz létre egy olyan listát, amelyben a duplikáció nem szerepel
my_list = [1, 1, 2, 3, 4, 5, 6, "alma", "körte", "alma"]

my_list2 = list(set(my_list))

#print(my_list2)

#2. feladat: irasd ki a megadott dictionary értékeit
auto_dict = {"márka": "Volvo", "szín": "Piros", "motor": "benzin", "hengerűrtartalom": 1.6}

#print(auto_dict.values())

#3. feladat: a megadott dictionary-hez adj hozzá tetszőlegesen egy új elemet.
auto_dict = {"márka": "Volvo", "szín": "Piros", "motor": "benzin", "hengerűrtartalom": 1.6}

auto_dict["teszt_elem"] = "teszt"
auto_dict.update({"teszt_elem2": "teszt2"})

#print(auto_dict)

#4. feladat: a megadott dictionary-ben márkához adjunk hozzá tetszőleges új értéket (pluszban a meglévőhöz).
auto_dict = {"márka": "Volvo",  "szín": "Piros", "motor": "benzin", "hengerűrtartalom": 1.6}

auto_dict["márka"] = "kuskutyafitty"
#print(auto_dict)

auto_dict.update({"márka": [auto_dict["márka"], "Ricsi"]})
#print(auto_dict)



#5. feladat: irasd ki a lista értékeit visszafelé
my_list = [1,2,4,5,6,7,8]
my_list.reverse()

print(my_list)

#print(my_list[::-1])

#6. feladat: a megadott lista elemei közül töröld a 2. és 3. Elemért
my_list = ["Elemér", "Elemér", "Elemér", ["Elemér", "Tamás"], "Géza", "Pista", "József"]

my_list.pop(2)
my_list.pop(1)

indexecske = my_list.count("Elemér")
print(indexecske)



#7. feladat: a megadott listában lévő beágyazott listának az elemeit "bontsuk ki", azaz konkatenáljuk a többi elemhez
my_list = ["Elemér", "Elemér", "Elemér", ["Zoltán", "Tamás"], "Géza", "Pista", "József"]

my_list = my_list[3] + my_list

#print(my_list)


# my_list.extend(my_list[3])
# my_list.pop(3)

#8. feladat: irassátok ki a páros számokat a megadott listából. használd a sort() metódust a listán való rendezéshez
my_list = [10, 3, 7, 2, 4, 9, 5, 6, 8 ]
my_list.sort()

#print(my_list[::2])

#9.feladat: irassátok ki a legnagyobb szám indexének értékét
my_list = [10, 3, 7, 2, 4, 9, 5, 6, 8 ]

my_list.index(max(my_list))

#my_list.sort()
print(my_list.index(max(my_list)))

print()

#10. feladat: a 2 megadott listát konkatenáljuk össze úgy, hogy ne legyen benne duplikáció
my_list = [2,3,4,5,6,7,8]
my_list2 = [2,3,4,9]

my_list3 = list(set([*my_list, *my_list2]))

print(my_list3)

[*my_list, *my_list2/0]








































