# absztrakciö


# egy class: objektumnak a tervrajza
class Animal:
    pass


elso_allat = Animal()

# print(Animal)
# print(elso_allat)

# self az intance-ot , objektumot magát jelenti
# cls

# __ dupla underscore-os függvényeket - > dunderscore -> double underscore
class Animal:
    def __init__(self, name, age):
        # nem vagy köteles ugyan azon a néven létrehozni az instance változót, mint ahogy a paraméterben megadod
        self.name = name 
        self.age = age
    
    # destructor
    # garbage collector elvégzi a destructor szerepét

    def __del__(self):
        print("Töröltem a példányt")
    


elso_allat = Animal("Floki", 2)




del elso_allat

# print(elso_allat.name)
# print(elso_allat.age)