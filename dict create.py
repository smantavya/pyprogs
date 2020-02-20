d = {}
b = 0
l = []
def key():
    b = input('key = ')
    if b not in l:
        d[b]=input('value = ')
    if b in l:
        print('key already exists')
        key()

while len(l) < 2:
    l = list(d.keys())
    key()

print(d)
