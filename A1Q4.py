n=int(input("enter the amount"))
h = n//100
print( h," notes of 100 rupees")
r1= n%100
f=r1//50
print(f, "notes of 50 rupees")
r2=r1%50
t=r2//10
print(t, "notes of 10 rupees")
