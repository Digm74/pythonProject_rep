def nod(a,b):
    while b > 0:
        a, b = b, a % b
        return a

def nok(a,b):

    c = (a*b)/nod(a,b)
    return c

print(nod(14,18))
print(nok(14,18))
