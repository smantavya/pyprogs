n = input('your word here = ')

s = 0
l = len(n)
b = 0
c = 0
for a in range(0,l):
    b = n.count(n[a])
    if b > s:
        s = b
        c = n[a]

print(c)
