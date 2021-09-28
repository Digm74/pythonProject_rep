# вложенные циклы
# for j in range(1,10):
#     for i in range(1,9):
#         print(i,'*',j, '=', i*j, ' ', end='')
#     print()
print('Эта' ' ' 'Программа')
print('''"Демонстрирует работу вложенных циклов"''')

from string import printable
for b1 in printable:
    for b2 in printable:
        for b3 in printable:
            print(b1,b2,b3)
            input()
