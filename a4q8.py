s = input("Enter string: ")
a= d = False

for i in s:
    if i.isalpha(): a= True
    if i.isdigit(): d = True
if a and d:
    print("alphabet digit both present")
elif not d:
    print("digit not present")
elif not a:
    print("alphabet not present")
else:
    print("not alphabet string present")


