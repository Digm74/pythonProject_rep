# СПИСКИ И ИХ МЕТОДЫ
a = [20, 40, 60, 80]
b = a[:]
b.append(100) # добавляеи в конец списка значение 100
print('Метод b.append(100) добавляет в конец списка b значение 100', '\n Список a: ', a, '\n Список b:', b, '\n', 'Длинна списка a: ', len(a), '\n', 'Длинна списка b: ', len(b))
c = a.copy()
print('Метод c = a.copy() создает копию списка а и присваивает его переменной с', '\n', c)
c.clear()
print('Метод c.clear() очищает список', '\n', c)
print('Метод a.count(40) подсчитывает сколько раз в списке встречается значение 40. '
      'Оно встречается ', a.count(40), 'раз.')
b.append(40) # добавляеи в конец списка значение 40
b.append(80) # добавляеи в конец списка значение 80
print(b)
print('Метод a.index(40,1,7) производит поиск сколько раз встречается значение '
      '40. Встречается ', a.index(40,1,7), ' раз.')
t = 40 in b[1:7]
print('данны метод производит проверку на наличие значения 40 в диапазоне от 1 до 7 и возвращает '
      'логическое значение (40 in b[1:7]) -- ', t)
a.insert(0,100) # Вставляет в первую позицию списка a значение 100
print(a)
# Метод pop удаляет с конца списка одно значение, задавая индексы можно проводить удаление из любой позиции списка
w = b.copy()
l = w.pop()
print(b, '\n', w, '\n', l)
b.reverse()
print(b, 'Метод b.reverse() Переворачивает список b')
a.sort(reverse=True)
print(a, 'Метод a.sort(reverse=True) сортирует список a по убыванию, a.sort() -- по возрастанию')

