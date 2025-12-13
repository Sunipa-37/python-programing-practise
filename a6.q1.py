l=list(input("enter few numbers").split())
l2=[]
for i in range (0,len(l)):
    j=(l[:i]+l[i+1:])
    if j not in l2:
        l2.append(j)
print(l2)