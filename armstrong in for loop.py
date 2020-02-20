a = int(input('start = '))
b = int(input('end = '))

for n in range(a,b+1):
    ln = len(str(n))
    s = 0
    temp = n

    while temp > 0:
        d = temp % 10
        s = s + (d ** ln)
        temp = temp//10

    if s == n:
        print(n)
