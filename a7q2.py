d={"a":"b","c":"d","e":"f","g":"h"}
l=list(d.keys())
k=input("enter new keys: ")
if k in l:
    print("key already exist")
else:
    v=input("enter value")
    d[k]=v
print(d)