a = int(input("first number = "))
b = int(input("second number = "))

if a < b:
    x = a
else:
    x = b

while x > 0:
    if a % x == 0 and b % x == 0:
        print("gcd =",x)
        x = 0
    else:
        x = x - 1

