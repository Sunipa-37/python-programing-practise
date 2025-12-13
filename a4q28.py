s = input("Enter a string: ")

count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        print(s[i], "=", count)
        count = 1

# print last character group
print(s[-1], "=", count)
