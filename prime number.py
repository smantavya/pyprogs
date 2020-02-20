n = int(input('your number here = '))
a = 2
while a < n:
    if n % a == 0:
        print(n,'is not a prime number')
        a = a+1
        break
    else:
        a = a + 1

if a == n:
    print(n,'is a prime number')


# for a in (2,n):
#     if n % a == 0:
#          print(n,'is not a prime number')
#          break
#     else:
#         continue
#
# else:
#     print(n,'is a prime number')
