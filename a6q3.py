a=[1,2,3,4,5]
b=[10,20,30,40,50]
k=int(input())
r=[]
rotate=a[-k:]+a[:-k]
for i in range(len(a)):
    r.append(rotate[i]+b[i])
print(r)