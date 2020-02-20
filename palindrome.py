s = input("enter your word here ")

l = len(s)
n = l//2
print(n)
if s[:(n):1]==s[l:n:(-1)]:
    print ("this is a palindrome")
else:
    print ("this is not a palindrome")
print(s[:(n):1])
print(s[l:n:(-1)])
