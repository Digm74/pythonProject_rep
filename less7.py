# УСЛОВНЫЙ ОПЕРАТОР WHILE
guess = input('Ведите пароль: ')
password = 'qwerty'
count = 0
while guess != password:
    print('Неверный пароль, повторите ввод')
    guess = input('Ведите пароль: ')
    count = count + 1
print('Вы сделали ', count, ' попыток')

a = [1, 2, 3, 4]*3
print(a)
while 3 in a:
    a.remove(3)
    print(a)