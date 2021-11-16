# inheritencia - öröklődás
# encapsulation - egységbe zárás
# polimorphism - polimorfizmus

class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Szalad")
    
    def atnevez(self):
        self.name = self.name[1:3]


class Dog(Animal):
    def __init__(self, age, name):
        #Animal.__init__(self, name)
        super().__init__(name)
        self.atnevez()
        self.age = age       

    def ugat(self):
        print(f"{self.name} ugat és {self.age} éves")


floki = Dog(2, "Floki")

#print(floki.__age)

floki.ugat()

floki.ful = "Nagy"

print(floki.ful)