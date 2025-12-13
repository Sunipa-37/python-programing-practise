s=input()
n=int(input())
while(n>0):
    s=s[-1]+s[0:-1]
    print(s)
    n-=1