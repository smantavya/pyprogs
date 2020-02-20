#
# #replace string function
#
# n = input('enter your word = ')
#
# s = input('enter word to replace = ')
#
# z = input('enter word to be replaced with = ')
#
# sind = n.index(s)
#
# m = n[0:sind] + z + n[sind+1:]
#
# print(m)

n = input('enter your word here = ')
b = ''
for a in range(0,len(n)):
    print(n[0:a+1])
