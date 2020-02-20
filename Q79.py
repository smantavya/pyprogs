n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = input('enter your element = ')
    l.append(b)

for b in l:
    c = l.count(b)
    if c > 1:
        d = l.index(b)
        l.remove(b)
    else:
        continue

print(l)
