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

s = 'qwerty134678QWE,.JK:'
while len(s)>0:
    bukva = s[0]
    if bukva > 'a' and bukva < 'z':
        print(bukva, 'is small')
    elif bukva > 'A' and bukva < 'Z':
        print(bukva, 'is big')
    elif bukva > '0' and bukva < '9':
        print(bukva, 'is digit')
    else:
        print(bukva, 'is simbol')
    s = s[1:]





