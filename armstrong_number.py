n = int(input("your number here "))

ln = len(str(n))
s = 0
temp = n

while temp > 0:
    d = temp % 10
    s = s + (d ** ln)
    temp = temp//10

if s == n:
    print("this is an armstrong number")
else:
    print("this is not an armstrong number")
