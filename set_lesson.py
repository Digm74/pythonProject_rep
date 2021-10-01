a = {1, 2, 3, 4, 1, 2, 6, 7, 3, 4, 9}
a.add(11)
a.add(9)
a.update('hello')
a.update(range(10))
a.update([11,56,33])
a.update({55,44,88})
a.discard(55)
a.remove(88)
print(a, type(a))
print(len(a))
print(11 in a, 55 not in a)
# операции над множествами
c = {1, 2, 3, 4}
e = {1, 4, 5, 6, 7}
print(c & e)  # операция ПЕРЕСЕЧЕНИЕ
print(c, e)
c &= e
print(c, e)
print(c.intersection(e))
print(c.union(e))  # Объединение множеств
print(e - c)  # вычитание
print(e ^ c)  # симметричная разность
print(c<e) # можно выполнять операции сравнения
for i in e:
    print(i)



# a.clear()
# b = {'ho', 'ni', 'no', 'hu', 'hi', 'hi'}
# c = set('Hello World')
# g = set(range(10))
# f = set()
# e = list(set(a))

# print(b)
# print(c)
# print(g)
# print(f)
# print(e)
