

a = [[0, 20, 30, 40], [1, 2, 3, 4], [11, 12, 13, 14], [21, [101, 105, 200, 300], 23, 24]]
s = ['the', 'best', 'way', 'no', 'this', 'english']
t=[
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11]
]
for i in t:
    for j in i:
        print(j, end=' ')
    print()

for i in range(3):
    for j in range(4):
        t[i][j]+=20
        print(t[i][j], end=' ')
    print()
print(t)

# print(t)
# print(len(a))
# print(a[3][1][3])
# print(s[0], s[1], s[2])
# print(s[3], s[2])
# print(s[5][-2])