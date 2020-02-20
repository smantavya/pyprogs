sample = ['p','q']
n = int(input('enter number of repeatation = '))
l = []
for a in range(1,n+1):
    b = sample[0] + str(a)
    l.append(b)
    c = sample[1]+str(a)
    l.append(c)

print(l)
