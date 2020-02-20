n = int(input("your number here "))

s = 0
temp = n
while n > 0:
    d = n % 10
    i = 1
    f = 1
    while i <= d:
        f = f*i
        i = i + 1
    s = s + f
    n = n//10
print(temp)
print(s)
if s == temp:
    print("this is a strong number!")
else:
    print("this is not a strong number!")
