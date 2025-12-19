l = list(map(int, input("Enter numbers separated by spaces: ").split()))
k=int(input("enter window size : "))

l1=[]
for i in range(0,k):
    l1.append(l[i])
    

print(l1)