a=input()
b=input()
c=0
d=''
for i in a:
    if i not in b and i not in d:
        print(i ,"is not present in ",b)
        d+=i
        continue
    c+=1
if d=='':
    print("True")
else:
    print("False")