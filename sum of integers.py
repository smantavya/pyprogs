# n = int(input("your three digit number = "))
#
# c = n % 10
# a = n // 100
# b = (n // 10) - (a*10)
#
# if a == b or b == c or a == c:
#     sum = 0
# else:
#     sum = a + b + c
#
# print(a,b,c)
# print(sum)

x = int(input("your first number = "))
y = int(input("your second number = "))
z = int(input("your third number = "))

if x == y or y == z or z == x:
    print("sum = 0")
else:
    print(x+y+z)
