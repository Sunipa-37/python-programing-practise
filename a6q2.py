sales=[[5,3,0,2],[7,0,2,1],[0,1,4,0]]
total=[0,0,0,0]
for i in sales:
    for j in range(0,len(i)):
        total[j]+=i[j]
print(total)

ma=max(total)
mi=min(total)
print("\n\n")
for i in range(0,len(total)):
    print("total sales of ",i+1," th product is",total[i])
    if total[i]==ma:
        print("maximum sold product ")
    elif total[i]==mi:
        print("minimum sold product")
    else:
        continue

