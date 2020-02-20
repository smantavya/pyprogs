name = input("enter your name ")
s1 = int(input("enter your marks in s1 "))
s2 = int(input("enter your marks in s2 "))
s3 = int(input("enter your marks in s3 "))
s4 = int(input("enter your marks in s4 "))
s5 = int(input("enter your marks in s5 "))


if s1<100 and s2<100 and s3<100 and s4<100 and s5<100:
        print("name = ", name)
        print("s1 =", s1)
        print("s2 =", s2)
        print("s3 =", s3)
        print("s4 =", s4)
        print("s5 =", s5)
        print("total = ", s1+s2+s3+s4+s5)
        print("percentage = ", (s1+s2+s3+s4+s5)/5)

x = ((s1+s2+s3+s4+s5)/5)
y = 60
z = 40
if x>=y:
    print("division = ", "1st")
if x>z and x<y:
    print("division = ", "2nd")
if x<z:
    print("division = ", "3rd")

p = 33
if x>p and s1>p and s2>p and s3>p and s4>p and s5>p:
    print("PASS")
else:
    print("FAIL")




#if s1>35 and s2>35 and s3>35 and s4>35 and s5>35



