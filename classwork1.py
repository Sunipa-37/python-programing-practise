s=input(" enter anything: ").lower()
s1=''
for i in s:
    if i not in s1:
        o=s.count(i)
        print("occureance of " ,i ,"is :",o)
        s1=s1+i
    
    
