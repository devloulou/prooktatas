import my_module_2

print(f"Létrehozáskor akkor a __name__ beállítva: {__name__}")

a = [1,2,3]

almafa = "almafa"

name = 'Ricsi'

def kiir():
    print('alama')

if __name__ == '__main__':
    print("My_module akkor fut, amikor közvetlen ezt futtatjuk")
else:
    print("my_module akkor fut, amikor importáljuk")