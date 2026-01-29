n=int(input("enter number of box"))
l=[]
for i in range(0,n):
    i=int(input("number of candies:"))
    l.append(i)
i=0
s=0
while(len(l)>1):
    c=l[0]+l[1]
    s+=c
    l[1]=c
    l=l[1:]
print(s)
