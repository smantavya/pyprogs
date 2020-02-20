# n = int(input('your number here = '))
# a = 2
# b = 2
# while b < n:
#     while a < b:
#             if b % a == 0:
#                 b = b + 1
#                 a = a + 1
#                 break
#             else:
#                 a = a + 1
#     if a == b:
#         print(b)
#     b = b + 1
#     if b == n:
#         break


a = int(input("Start "))
b = int(input("End "))

for q in range(a,b+1):
    for r in range(2,q):
        if q%r == 0:
            break
    else:
        print(q)
