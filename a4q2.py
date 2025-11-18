s=input("enter binary digits: ")
n=len(s)
result=0
for i in s:
    if i=='1': d=1
    elif i=='0': d=0
    else:
        print("invalid input")
        break
    
    result+=(d*pow(2,n-1))
    n-=1
print(result)
