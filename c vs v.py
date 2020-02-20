a = input('enter your word = ')
a = a.upper()

c = 0
# c will gain point for every consonants
v = 0
# v will gain point for every vowels

n = 0
# n is index number in 'a'

l = len(a)

while n < l:
    if a[n] in ('AEIOU'):
        v = v + (l-n)
        n = n + 1
    else:
        c = c + (l-n)
        n = n + 1

print('points for c =',c)
print('points for v =',v)

if c > v:
    print('KO! c wins!')
else:
    print('KO! v wins!')
