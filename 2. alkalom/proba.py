lista = [1,2,3]

lista.extend(['anyukam', 1])

print(list(set(lista)))

num = 1.3

print('Hey, this is %(float)f' % {'float': num})
print('Hey, this is {data:f}'.format(data=num))
print(f'Hey, this is {num:#f}')