########################
lista_new = [1,2,3]

lista_new_2 = lista_new

#lista_new.remove(2)

print(lista_new_2)

print("#######################")
print(lista_new == lista_new_2)

lista_new_2 = list(lista_new)

lista_new.remove(2)

print(lista_new_2)
print(lista_new)

#print(lista_new == lista_new_2)
print("#######################")
print(hex(id(lista_new)))
print(hex(id(lista_new_2)))


#######################