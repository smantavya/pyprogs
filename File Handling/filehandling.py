file = open('test.txt','w')
# file.write('welcome to Ws Cube Tech\n')

l = ['abc','def','ghi']
for a in range(len(l)):
    l[a] = l[a] + '\n'
print(l)
file.writelines(l)

file.close()
