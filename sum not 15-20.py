n = int(input("your two digit number = "))

a = n // 10
b = n % 10

s = a + b

if s in (15,16,17,18,19,20):
    print("sum = 20")
else:
    print("sum =",s)
