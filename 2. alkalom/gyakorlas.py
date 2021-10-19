
my_list = []
my_lit2 = list()


# lista []
# tuple ()
# dictionary {}
# set {}


my_list.append(1)
my_list.append(2)
my_list.append(4)
my_list.append("Ricsi")

my_list.append([1,2,3,4,5,6])
# my_list.extend([1,2,3,4,5,6])

# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# my_list.append(6)

my_list.extend([
    ["piros", "zöld", "kék"],
    ["alma", "körte", "banán"] 
])

my_list.append(["piros", "zöld", "kék"])
my_list.append(["alma", "körte", "banán"])



# print(my_list)
# print(type(my_list[4]) )
# print(type(my_list[5]) )



my_lista3 = [1,2,3]

my_lista4 = ["alma", "körte"]
#my_lista5 = my_lista3 + my_lista4 + my_list
my_lista5 = []
my_lista5.extend(my_lista3)
my_lista5.extend(my_lista4)
my_lista5.extend(my_list)


# utolsó eleme a listának
# print(my_lista5[-1])

# print(my_lista5[-5])
# print(my_lista5[1])

#slicing
# print(my_lista5[4:])
# print(my_lista5[:4])
# print(my_lista5[-5:])
# print(my_lista5[-5:-2])
# print(my_lista5[4:9])
# print(my_lista5[4:9:3])
# print(my_lista5[::])
# print(my_lista5[::2])
# print(my_lista5[:-2])


# my_lista5[:my_num:my_leptek]
# my_lista5.clear()

print(len(my_lista5))
#del my_lista5
my_lista5.append('alma')

print(my_lista5)

# érték mentén törölni
my_lista5.remove('alma')
#my_lista5.remove('alma')
print(my_lista5.pop(7))

print(my_lista5[9].remove('alma'))

print(my_lista5[9])

# index mentén törölni
# my_list.remove()
# my_list.pop()
# print(my_lista5)
print()
print()
print()


tlist = [1,2]
# ésszel, mert ezzel nagyon nagy károkat és több órás debugot tudsz okozni
tlist2 = tlist

print(tlist == tlist2)
tlist.remove(1)
tlist.append('Ricsi')

tlist2.remove(2)


print(tlist)
print(tlist2)

tlista_3 = [1,2,3,4,5,6,7]

#insert egy megadott index helyre
tlista_3.insert(0, "Béla")
tlista_3.insert(10005, "Béla")
tlista_3.insert(2, "Béla")
print(tlista_3)

##########################################################
#Tuple - Immutable - Megváltoztathatatlan - Nem lehet módosítani: nem lehet hozzáadni, törölni, nem lehet összeadni
# slicing működik
print()
print()
print()
proba_tuple = ()



my_lista_test = [1, 1, 1, 2, 3, 4, 5,6124,\
                    "Ricsi", "Jocó", "sütemény",\
                    [1, 1, 2],\
                    ("Ricsi", "Jocó"), print]

my_tuple = tuple(my_lista_test)

my_tuple2 = my_tuple

print(hex(id(my_tuple2)))

del my_tuple

print(my_tuple2)
print(my_tuple2)


# print(my_tuple.count(1))
# print(my_tuple[4:])
# print(my_tuple.index("sütemény"))

# print(my_tuple[::])
# print(my_tuple[::2])
# print(my_tuple[:-2])

# dictionary
# kulcs:érték párokból áll, kulcs unique: nem lehet duplikáció
print()
print()
print()

my_dict = {}
my_dict_pre = dict()

my_dict_pre2 = {"autó_színe":"zöld"}

dict_list = [2,3,4]
dict_tuple = tuple(dict_list)

my_dict["autó_typus"] = "toyota"
my_dict["autó_typus"] = "opel"

my_dict.update({"autó_színe":"zöld"})
my_dict.update({"autó_színe":"piros"})

my_dict.update({print : "hülység" })

my_dict.update({dict_tuple: "hülység"})

print(my_dict)
#my_dict.clear()
#my_dict.pop("autó_színe")
#my_dict.popitem()
#del my_dict["autó_typus"]
print(my_dict)
print(my_dict.keys())

list(my_dict.keys()).pop(1)

test_list = [1,2,2,2,3,4]

deduplication = list(set(test_list))
str(test_list)

print(test_list)
print(type(test_list))
exit()
#print(my_dict.values())

print(my_dict.keys())
print("---------------------")


print(my_dict["autó_typus"])
#print(my_dict["Ricsi"])

print(my_dict.get("Ricsi", None))
