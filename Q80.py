n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = input('enter your element = ')
    l.append(b)

if len(l) != 0:
    print('list is not empty.')
else:
    print('list is empty.')
