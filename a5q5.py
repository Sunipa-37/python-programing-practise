s=input("enter few small word").split()
match={}
for i in s:
    k="".join(sorted(i))
    if k not in match:
        match[k]=[]
    match[k].append(i)
r=list(match.values())
print(r)