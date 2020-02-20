n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = input('enter your element = ')
    l.append(b)

n2 = int(input('enter number of elements in list = '))

l2 = []


for a2 in range(n2):
    b2 = input('enter your element = ')
    l2.append(b2)

for c in l:
    d = c
    if d in l2:
        print('true')
        break
    else:
        continue

