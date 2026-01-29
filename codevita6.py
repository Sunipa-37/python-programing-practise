n=int(input("total numbers of team:"))
d=dict()
for i in range(n):
    i=input("team name:").lower()
    d[i]=0
d1=dict(sorted(d.items()))
m=int(input("number of matches:"))
for i in range(m):
    t1=input("team 1:").lower()
    t2=input("team2:").lower()
    if(t1==t2):
        exit()
    d1[t1]=d1[t1]+int(input("team 1 score:"))
    d1[t2]=d1[t2]+int(input("team 2 score:"))
l=[0] 
for i in d2.values():
    l.append(i)
print(L)
