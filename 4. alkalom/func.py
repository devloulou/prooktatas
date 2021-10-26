def kiir():
    my_list = [1,2,3,40]
    my_dict = {"kukcs": "érték"}
    a = 100
    return my_list, my_dict, a

valtozo = kiir()
valtozo[0]

val_list, val_dict, val_a = kiir()

print(val_list)
print(val_dict)
print(val_a)

#print(type(valtozo))

def kiir():
    my_list = [1,2,3,40]
    my_dict = {"kukcs": "érték"}
    a = 100
    return [my_list, my_dict, a]


