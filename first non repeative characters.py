n = input('enter your word = ')

l = len(n)

# for a in range(0,l):
#     d = n[a]
#     b = n.count(d)
#     if b == 1:
#         print(d)
#         break
#         continue


for q in range(l):
    if n[q] not in n[q+1:] and n[q] not in n[0:q]:
        print(n[q])
        break
