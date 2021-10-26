import os
# tuple, list - dictionary
# comprehension

# for item in range(1,6,2):
#     print(item)

# my_list = []
# for item in range(1, 1000):
#     if item%2 == 0:
#         my_list.append(item)



# print(len(my_list))

# my_list2 = [item  for item in range(1, 1000) if item%2 == 0 ]


# print(len(my_list2))


# feldat: egy megadott mappából listázd ki a file-okat
#import os

my_list = []
for file in os.listdir(r"C:\\WORK\\Prooktatás\\1. lesson\\prooktatas\\4. alkalom"):
    my_list.append(file)

#print(my_list)

my_list2 = [file for file in os.listdir(r"C:\\WORK\\Prooktatás\\1. lesson\\prooktatas\\4. alkalom")]

# generator expression
# függvény
# prototype-olás
def osszegyujt():
    pass

def torli():
        pass

def futtat():
 pass

def valami():
  pass


# visszatérési érték nélküli megadás


# visszatérési értékkel való magadás
def kiir(message):
    return message

def kiir(message):
    print(message)

szam = 10

#kiir("Hello, world")
#print(kiir("Hello, world"))
#a = kiir("Hello, world")

b = kiir

#print(b)



   




# packing - unpacking

my_list = [1,2]
my_list2 = [3,4]
my_list3 = [*my_list, *my_list2]

#print(my_list3)

my_list = ["Pisti", "Józsi", "Karcsi"]

def kiir(nev1, nev2, nev3, nev4="Julcsi"):
    print(f"Szia {nev1}")
    print(f"Szia {nev2}")
    print(f"Szia {nev3}")
    print(f"Szia {nev4}")

#kiir('Ricsi', 'Józsi', 'Norbi', 'Jozsó')

# unpacking: mert kibontjuk a megadott listát 
#kiir(*my_list)

# *args  - **kwargs -> dictionary megadása
def kiir(*args):
    print(type(args))
    print(len(args))

    for item in range(0, len(args)):
        #print(item)
        print(args[item])

# packing
kiir(1,2,3,"Ricsi")



def kiir(**kwargs):
    print(type(kwargs))
    print(kwargs)

    for key, value in kwargs.items():
        print(f"{key} - {value}")

my_dict = {"auto": "Golf", "pénz": "Euró"}

kiir(a="Real", b="Python", c="Is", d="Great", e="!")

def kiir(*args, **kwargs):
    print(args)
    print(kwargs)


kiir("Ricsi", "Norbi", auto="Golf", szín="piros")

import os

lista = os.__name__

print(print.__name__)
print(lista)






