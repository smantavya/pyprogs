file=open("hello.txt","a")




file.write("Welcome to IIP\n")
file.write("Welcome to IIP\n")
file.write("Welcome to IIP\n")
file.write("Welcome to IIP\n")



l=["hello","ABC"]

# file.writelines(l)
for a in l:
    file.write(a+"\n")

file.close()
