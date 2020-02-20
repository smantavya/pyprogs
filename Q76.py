n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = input('enter your element = ')
    l.append(b)

for c in l:
    for d in l:
        if d >= c:
            e = d
            break
        else:
            continue

print(e)
