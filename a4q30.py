s = input("Enter main string: ")
sub = input("Enter substring to delete: ")

while True:
    pos = s.find(sub)   # find substring

    if pos == -1:       # not found → stop
        break

    # delete substring using slicing
    s = s[:pos] + s[pos + len(sub):]

if s == "":
    print("YES, the string can become empty")
else:
    print("NO, the string cannot become empty")
