file=open("hello.txt","r")
#
# print(file.read())
#
# print(file.tell())
#
# print(file.seek(0))
#
# print(file.read(5))
#
# print(file.read())

# print(file.readline(5))
# print(file.readline())
# print(file.readline())
#

l=file.readlines();
print(l)

for a in l:
    print(a,end="")

file.close()
a=10
b=20
print(a<<20)
