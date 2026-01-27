p=500000
t=26
s1=3
mir1=[9.5,6.9,5.6]
noy1=[13,3,10]
emi_a=0
for i in range(3):
    e=p*mir1[i]/(1 - 1 /(1+ mir1[i])**(noy1[i]*12))
    emi_a+=e
s2=3
mir2=[8.5,7.4,9.6]
noy2=[14,6,6]
emi_b=0
for i in range(3):
    e=p*mir2[i]/(1-1 /(1+ mir2[i])**(noy2[i]*12))
    emi_b+=e
print(emi_a, emi_b)
if(emi_a < emi_b):
    print(" bank a")
else:
    print("bank b")
