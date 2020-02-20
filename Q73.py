n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = input('enter your element = ')
    l.append(b)

a = l[n-1]
b = l[0]

l[0] = a
l[n-1] = b

print(l)
