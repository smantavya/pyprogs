a = int(input("1st number = "))
b = int(input("2nd number = "))

x = 1


if a < b:
    y = a
else:
    y = b

while x > 0:
    if x % a == 0 and x % b == 0:
        print("lcm =",x)
        x = 0
    else:
        x = x + 1
