num = input('Введите число: ')
kol = int(len(num))
a = int(num) // 10 ** (kol-1)
b = (int(num) // 10 ** (kol-2)) % 10
c = (int(num) // 10 ** (kol-3)) % 10
d = (int(num) // 10 ** (kol-4)) % 10
e = (int(num) // 10 ** (kol-5)) % 10
w = int(num)  % 10
print (num, kol)
print(a, b, c, d, e, w)