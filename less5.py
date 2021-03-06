# Списки: индексы и срезы
# Порядковый номер элемента в списке
#     0   1   2   3   4   5   6   7   8  9
a = [23, 34, 43, 56, 67, 44, 22, 11, 89, 9]
# Порядковый номер элемента в списке
#    0  1  2  3  4  5  6  7  8  9  10
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a)
print('1-й элемент: ', a[0])
print('3-й элемент: ', a[3])
print('6-й элемент: ', a[6])
print('8-й элемент: ', a[8])
print('------------------------------------------------------------')
# Можно получать список элементов списка с конца
print('10-й элемент: ', b[-1])
print('8-й элемент: ', b[-3])
print('5-й элемент: ', b[-6])
print('2-й элемент: ', b[-9])
print('------------------------------------------------------------')
print(b[1:6], 'Можно указывать диапазон вывода элементов списка. При этом 6-й элемент выводится не будет')
print(b[1:], 'Будут выведены все элементы')
print(b[1:99], 'Будут выведены все элементы')
print(b[1:-1], 'Выведутся с 1-го по 9-ый')
print(b[:3], 'Выведутся с 1-го по 2-й')
print(a[:], 'Выведутся все элементы')
print(a[::2], 'Можно задавать шаг вывода')
print('------------------------------------------------------------')
print(b[::-1], 'Перевернет список')
print('------------------------------------------------------------')
d = b[:] # Создаёт копию списка b
d[1] = 100 # Присвоим 1-у элементу значение 100
print(b,'\n', d)
e = a[:] # Создаёт копию списка a
e[1:5] = 200, 30 # Присвоим 1-у и 2- му элементу значение 200 и 30 элементы 3 и 4 будут удалены
print(a, '\n', e)
del d[3] # УДаляет 3-й элемент списка
print(b,'\n', d)