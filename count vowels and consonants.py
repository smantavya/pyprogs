n = input('enter your word = ')

l = len(n)
v = 0
c = 0

for a in range(l):
    d = n[a]
    if d in ('aeiou'):
        v = v + 1
    else:
        c = c + 1

print('number of vowels =',v)
print('number of consonants =',c)
