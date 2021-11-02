
import my_module as al
#from my_module import a
#from my_module import *

print(f"Létrehozáskor akkor a __name__ beállítva: {__name__}")

b = [5,6,7]

a = [7,8,9]
# print(a)

al.kiir()

def kiir():
    print("beka")


#print(name)

if __name__ == '__main__':
    print("My_module_2 akkor fut, amikor közvetlen ezt futtatjuk")
else:
    print("my_module_2 akkor fut, amikor importáljuk")