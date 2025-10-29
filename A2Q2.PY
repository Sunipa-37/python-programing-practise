r=int(input("enter ram's age: "))
s=int(input("enter shayam's age: "))
a=int(input("enter ajay's age: "))

if r<s:
    if (r<a):
        print("ram is youngest")
    else:
        print("ajay is youngest")
elif a<s:
    if(a<r):
        print("ajay is youngest")
    else:
        print("ram is youngest")
else:
    print("shyam is youngest")

