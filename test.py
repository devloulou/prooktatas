print('valami')

a = 2
#print(type(a))

a = 2.0
#print(type(a))

a = 0xA0F
#print(type(a))

a = 0o37
#print(type(a))

a = 2+3j
#print(type(a))

a = "Ricsi"
#print(type(a))
###################################

# lista
elso_lista = ["alma",   [], {}, (), print,   None, \
                               1]
masodik_lista = list(a)

print(elso_lista)

# tuple
elso_tuple = ("alma", 1, None)
masodik_tuple = tuple()

# dictionary
elso_dict = {"kulcs": "érték",
                            'autó': 'toyota',
            "elso_lista": elso_lista,
            "elso_dict": {
                "kulcs": {
                    "kulcsocska": masodik_tuple
                    }
            }            
            }
masodik_dict = dict()

# set and collection
# print(elso_lista, elso_dict,\
#      elso_dict, elso_dict, elso_dict,elso_dict )