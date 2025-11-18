s=input("enter anything").lower()
v='aeiouAEIOU'
for i in s:
    if i in v:
        a=ord(i)
        a+=1
        b=chr(a)
        print(b,end='')
    else:
        print(i,end='')
