n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = str(input('enter your element = '))
    l.append(b)

o = input('enter word = ')

for b in l:
    if len(b) > len(o):
        print(b)
