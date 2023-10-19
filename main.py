list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 8]
print(list_1)
print(*list_1)

for i in list_1:
    print(i)

print(len(list_1))
print(list_1[0])
print(list_1[-1])

list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)

list_1 = []
for i in range(5):
    list_1.append(i)
print(list_1)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) # [9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]

t = () # кортеж (tuple)
print(type(t))
t = (1)
print(type(t))
t = (1, )
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))
v = tuple(v)
print(v)
print(type(v))
# a, b = 1, 2
# a = b = 1
a, b, с = v
print(a, b, с)

t = (1, 2, 3, 5, )
print(t[1])
for i in t:
    print(i)
print()
for i in range(len(t)):
    print(t[i])

d = {} # словарь
d = dict() # словарь
d['q'] = 'qwerty'
print(d)
d['w'] = 'werty'
print(d)
print(d['q'])

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐' 
print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type' Такого ключа не существует
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k, v) in dictionary.items():
    # print(item)
    print('{}: {}'.format(item, dictionary[item]))
for (k, v) in dictionary.items():
    print(k, v)
print(dictionary.items())
dictionary[895] = 98998
print(dictionary)

# множества set
colors = {'red', 'green', 'blue'}
print(colors) # {'green', 'red', 'blue'}
colors.add('red')
print(colors) # {'green', 'red', 'blue'}
colors.add('gray')
print(colors) # {'green', 'red', 'gray', 'blue'}
colors.remove('red')
print(colors) # {'green', 'gray', 'blue'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red')
print(colors) # {'green', 'gray', 'blue'}
colors.clear() # { } Удалить все элементы
print(colors) # set()

a = {1, 8, 6}
b = frozenset(a)
print(b)

list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]

list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
print(list_1)

list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
print(list_1)

list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
print(list_1)

ist_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
