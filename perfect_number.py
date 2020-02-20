n = int(input("your number here "))

i = 1
s = 0
while i < n:
        if (n % i == 0):
            s = s + i
            i = i + 1
        else:
            s = s + 0
            i = i + 1


if s == n:
    print("this is a perfect number")
else:
    print("this is not a perfect number")
