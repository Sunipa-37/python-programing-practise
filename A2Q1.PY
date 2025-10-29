c=int(input("cost price"))
s=int (input("selling price"))
if s>c:
    print("made profit of rupees: ",s-c)
elif s<c:
    print("incurred loss of ruppes: ",c-s)
else:
    print("no profit no loss")