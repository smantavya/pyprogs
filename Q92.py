d = {0:0,1:1,2:4,3:9,4:16,5:25}

l = list(d.keys())

print(l)

a = int(input('enter the value to find = '))

if a in l:
    print('True')
else:
    print('false')
