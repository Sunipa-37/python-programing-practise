s=input("enter a string of positive integer: ")
s=s.split()
b=[]
c=[s[0]]
for i in range (1, len(s)):
    ds1=sum(int(d) for d in s[i])
    ds2=sum(int(d) for d in s[i-1])
    if ds1>ds2:
        c.append(s[i])
    else:
        if len(c)>len(b):
            b=c
        c=[s[i]]
if len(c)> len(b):
    b=c
print("longest subsequence",b)
print("length ",len(b))

