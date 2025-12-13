s = input("Enter string: ")
r = s
for i in range(0,len(s)):

    s = s[1:] + s[0] 
    print(s) # left rotatio
    if r == s:
        print(i+1)
        break
