dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for i in dic1.keys():
    dic4[i]=dic1[i]
for i in dic2.keys():
    dic4[i]=dic2[i]
for i in dic3.keys():
    dic4[i]=dic3[i]
print(dic4)
