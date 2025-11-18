s=input("enter string of digits:")
n=0
for i in s:
    if i =='1': d=1
    elif i=='2':d=2
    elif i=='3':d=3
    elif i=='4':d=4
    elif i=='5':d=5
    elif i=='6':d=6
    elif i=='7':d=7
    elif i=='8':d=8
    elif i=='9':d=9
    elif i=='0':d=0
    else:
        print("invalid input")
        break
    
    n=d+(n*10)
print(n)
