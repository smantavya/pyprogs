n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = input('enter your element = ')
    l.append(b)
l.pop(0)
print(l)
