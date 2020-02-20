n = int(input('enter number of elements in list = '))

l = []


for a in range(n):
    b = int(input('enter your element = '))
    l.append(b)


l.sort(reverse=True)
c = l.count(l[0])
print(l)
print('second highest number is',l[c])




















# for c in l:
#     for d in l:
#         if d >= c:
#             e = d
#             break
#         else:
#             continue
#
# l.remove(e)
#
# for e in l:
#     for f in l:
#         if f >= e:
#             e = f
#             break
#         else:
#             continue
#
# print(e)
