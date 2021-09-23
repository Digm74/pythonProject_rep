# Алгоритм Евклида, наибольший общий делитель
# Вариант реализации №1
# a =int(input())
# b =int(input())
a, b = map(int, input().split()) # Такой метод ввода позволяет вводить числа через пробел
if a > 1000:
    while b > 0:
        a, b = b, a%b
    print(a)
    print('Число больше 1000 ')
else:
    # Вариант реализации №2
    while b != a:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)
    print('Число меньше 1000 ')

