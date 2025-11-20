s = input("Enter anythiing: ").lower()
vowels = "aeiou"
flag = True
for v in vowels:
    if v not in s:
        flag = False
        break
if flag:
    print("accepted")
else:
    print("not accepted")
