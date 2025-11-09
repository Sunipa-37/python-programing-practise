n=int(input("how many days you are late:"))
if n<=5:
    c=n*0.5
    print("fine amount:", c)
elif n<=10:
    c= 1*n
    print("fine amount: ",c)
elif n<=30:
    c=n*5
    print(" fine ammount: ",c)
else:
    print("membership cancelled ")