# Списки и операции над ними

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
s = ['stroka', 'helpmy', 'world', 'hello', 'bobik']
print(type(a))  # Тип переменной Type()
print(len(a))
print(s)
print(len(s))  # Длина спиская len()
print(a + s)  # Сложение двух списков
print(s + ['Hi'] + [5])  # К спискам можно жобавлять только списки если попытаться добавлять просто строки или числа
# будет ошибка
print(s * 2)  # При умнажении списка на число происходит повтор элементов
print(2 in a, 'hello' in s) # Проверяет наличие искомого значения в списке если есть то истина если нет то ложь
print(sum(a), max(a), min(a)) # Сумма элементов списка и максимальное минимальное значение элемента списка только для чисел
print(sorted(a))
print(sorted(s))
print(sorted(a,reverse=True))
print(sorted(s,reverse=True))
# Сравнение списков
print(a==b) # Можно сравнивать числа с числами
print(a>b) # Сравнивать на больше меньше можно списки с числами, если сравнивать с строковыми значаниями будет ошибка
print(a<b)
print(a==s) # Можно сравнивать числа со строками
print(sum(a)/len(a))
