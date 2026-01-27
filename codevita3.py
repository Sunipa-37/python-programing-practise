s=10
r=2
list=[345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
r1=[300,350]
r2=[400,700]
c=0
out=[]
for l in list:
    if l > r1[0] and l <r1[-1]:
        c+=1
out.append(c)
c=0
for l in list:
    if l > r2[0] and l <r2[-1]:
        c+=1
out.append(c)

print(out)
