l = [{'V':'S001'},{'V':'S002'},{'VI':'S001'},{'VI':'S005'},{'V':'S009'},{'VIII':'S007'}]
b = []
for a in l:
    if l[a].values() not in b:
        b = b.append(l[a].values())
