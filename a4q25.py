from itertools import permutations 
s = input("Enter a string: ") 
perms = permutations(s) 
print("Permutations are:") 
for p in perms: 
    print("".join(p))