# file megnyitása
# open() -> file helye, megnyitás módja, kódolás
f = open('C:\WORK\Prooktatás/1. lesson\prooktatas/6. alkalom/test_file.txt')

print(f)

print([line for line in f])

# seek(offset[, whence])
# sets the file's current position at the offset
# second argument:  whence − This is optional and defaults to 0 which means absolute 
# file positioning, other values are 1 which means seek relative to the current 
# position and 2 means seek relative to the file's end.

f.seek(5)

#f.write('hozzáírok\n')

# for line in f:
#     print(line)

f.close()

# file megnyitása
#f = open('file helye')
#f.close()

try:
    f = open('C:\WORK\Prooktatás/1. lesson\prooktatas/6. alkalom/test_file.txt')
finally:
    f.close()

#with - kontextusmanager
# https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/
# 'r'  -> read only
# 'r+' -> read and write
# 'w'  -> write only
# 'w+' -> write and read
# 'a'  -> write only append
# 'a+' -> read and write only append


with open('C:\WORK\Prooktatás/1. lesson\prooktatas/6. alkalom/test_file.txt', 'r') as f:
    for line in f:
        print(line)
        break

with open('alma.txt', 'w', encoding='utf-8') as f:
    f.write('Álmodtam egye érdekeset')
    f.write('Álmodtam egye érdekeset\n')
