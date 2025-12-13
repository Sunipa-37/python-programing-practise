s = input("Enter string: ")
for ch in set(s):
    if s.count(ch) % 2 != 0:
        print(ch, end=" ")
