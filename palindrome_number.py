s = int(input("enter your number here "))

l = len(str(s))
s=0
temp = s
while temp > s:
    d = s % 10
    s = s*10 + d
    n = n//10

if  temp == s:
    print("this is a palindrome number")
else:
    print("this is not a palindrome number")
