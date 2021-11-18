# encapsulation - egységbezárás:
# addig tarts a változóidat "private" , amíg meg interfacelése

class Dog:
    def __init__(self):
        self.__name = "Floki"

    def __str__(self):
        print(f"Name kiiír")
    
    def printer(self):
        print(self.__name)

    def __printer__(self):

        print("privát vagyok")
    
floki = Dog()

floki.printer()
#floki._Dog__printer()
#print(floki._Dog__name)

