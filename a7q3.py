d1={1:10,2:20,4:6}
d2={3:30,4:40,5:2}
d3={5:50,6:60}
d4=d1
d5=d2|d3
for i in d5.keys():
    if i in d4.keys():
        d4[i]+=d5[i]
    else:
        d4[i]=d5[i]
print(d4)
