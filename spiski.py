# НАПОЛНЕНИЕ СПИСКОВ
a = []
n = int(input())  # kol stolbcov
m = int(input())  # kol strok

# for i in range(n):
#     a.append([0] * m)
# for i in a:
#     print(i)

for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input()))
    a.append(b)
for g in a:
    print(g)










# a = [[0, 20, 30, 40], [1, 2, 3, 4], [11, 12, 13, 14], [21, [101, 105, 200, 300], 23, 24]]
# s = ['the', 'best', 'way', 'no', 'this', 'english']
#
# t=[
#     [0,1,2,3],
#     [4,5,6,7],
#     [8,9,10,11]
# ]
# ВАРИАНТЫ ОБХОДА СПИСКОВ
# for i in t:
#     for j in i:
#         print(j, end=' ')
#     print()
# print()
#
# for i in range(3):
#     for j in range(4):
#         t[i][j]+=20
#         print(t[i][j], end=' ')
#     print()
# print()
# print(t)
# print()
# for j in range(4):
#     for i in range(3):
#         # t[i][j]+=20
#         print(t[i][j], end=' ')
#     print()
# print()
# for i in range(2, -1, -1):
#     for j in range(3, -1, -1):
#         print(t[i][j], end=' ')
#     print()
# print()
#
# for i in range(3):
#     x = 0
#     for j in range(4):
#         x+=t[i][j]
#     print(x)
#
#









# print(t)
# print(len(a))
# print(a[3][1][3])
# print(s[0], s[1], s[2])
# print(s[3], s[2])
# print(s[5][-2])