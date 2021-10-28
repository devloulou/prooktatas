import copy

#my_list = [1, 2, 3]

# my_list2 = my_list
# my_list2.clear()
# print(my_list)


# 2: shallow copy
#    deep copy

# my_list = [1, 2, 3]

# my_list2 = copy.copy(my_list)

# print(id(my_list[0]))
# print(id(my_list2[0]))

# my_list[0] = -10

# print(id(my_list[0]))
# print(id(my_list2[0]))

# print(id(my_list[1]))
# print(id(my_list2[1]))


# print(my_list)
# print(my_list2)


my_list3 = [[1,2,3,4],3,4]

my_list4 = copy.deepcopy(my_list3)

my_list3[0][0] = -10

print(my_list3)
print(my_list4)

print(id(my_list3))
print(id(my_list4))