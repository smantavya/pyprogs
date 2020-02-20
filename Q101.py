#to sort a dictionery =

d = {0:0,1:1,4:16,3:9,2:4,5:25}

l = list(d.keys())

l.sort()

d.clear()

for a in l:
    d[a] = a**2

print(d)
