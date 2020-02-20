n = input('enter your word = ')
l = len(n)
for a in n:
    x = ''
    x = a
    for b in n:
        y = b
        if b not in x:
            x = x + y
    print(x)
