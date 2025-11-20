s1=input("enter anything").lower()
s2=input("enter anything").lower()
c=0
temp=''
for i in s1:
    if i in temp:
        break
    if i in s2:
        c+=1
        temp+=i
print(s1)
print(s2)
print(c)
