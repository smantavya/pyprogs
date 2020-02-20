a = input('enter your word = ')
l = len(a)
n = 0

while n < l:
    print(a[n],a.count(a[n]))
    n = n + 1
