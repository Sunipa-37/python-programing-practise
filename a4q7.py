s = input("enter anything: ")
s1 = ""

for i in s.split():
    if len(i) == 1:
        s1 += i.upper() + " "
    else:
        s2 = i[0].upper() + i[1:-1] + i[-1].upper()
        s1+= s2+ " "

print(s1)
