n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = int(input('enter your element = '))
    l.append(b)

for c in l:
    if c % 2 == 0:
        l.remove(c)

print(l)
