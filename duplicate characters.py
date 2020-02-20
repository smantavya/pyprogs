# n = input('enter your word = ')
#
# l = len(n)
#
# for a in range(0,l):
#     b = n[a]
#     c = n.count(b)
#     if c != 1:
#         d = n.index(b)
#         e = n[0:d]+n[d+1:l]
#         print(e)


h= input('enter your word = ')

n=''

for a in h:
    if a not in n:
        n=n+a

print(n)
