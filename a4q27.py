s=input("few names").split()
item=input()
c=1
for i in s:
    if i == item:
        print(c)
        break
    c+=1