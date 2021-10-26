# ciklusok

# for ciklusváltozó in iterálható valami
#       műveletek

# for item in 'alma':
#     print(type(item))

# while feltétel:
#   fut
#  teljeseül egy feltétel és kilép a ciklusból

# szam1 = 10
# while szam1 < 12:
#     print(szam1)
#     szam1 += 1



my_list = [12,3,4,5,6,7,8]

# tuple-ön, dictionary is igaz
#lista index for ciklus során

# for idx, item in enumerate(my_list):
#     print(f"{idx} - {item}")

my_tuple = (12,3,4,5,6,7,8)

my_str2 = "test"

my_str = "%s ricsi" %my_str2

print(my_str)

my_str = "ricsi"

my_str2 = f"ricsi {my_tuple}"

my_string = "ricsi {tupleke}".format(tupleke=my_tuple)

my_str3 = "ricsi" + "ricsi"
my_str4 = my_str + " - ".join(map(str, my_tuple))

my_tuple = (12,3,4,5,6,7,8)

print(my_str4)

#### 
# map(str, my_tuple)
# str(12)
# str(3)...

for item in map(str, my_tuple):
    print(item)

print(map(str, my_tuple))
print(type(my_str2))



for idx, item in enumerate(my_tuple):
    print(f"{idx} - {item}")
    print(str(idx) + '-' + str(item))

my_dict = {"key": "val", "auto": "mazda", "szin":"piros"}

# for item in my_dict.values():
#     print(item)

# for key, value in my_dict.items():
#     print(f"{key} - {value}")



my_list = [1,2,3,4,5]

osszeg = 0

# for item in my_list:
#     if item == 2:
#         pass
#     else:
#         osszeg += item

# for loop: continue, break
# for item in my_list:
#     if item == 2:
#         continue
#     else:
#         osszeg += item

# for item in my_list:
#     if item == 2:
#         continue
#     osszeg += item

for item in my_list:
    if item == 2:
        break
    if item == 1:
        break
    osszeg += item

for item in my_list:
    break

for item in my_list:
    continue

for i in my_list:
 pass


print(osszeg)

a = 10
b = 56



if 1 == 1:
    alma = "fa"
    print(alma)

print(alma)





















