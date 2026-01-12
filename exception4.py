class lessmarks(Exception):
    pass
class math(Exception):
    pass
percentg=int(input("enter your percentage of ug:"))
caste=input("enter your caste:").lower()
jeca=int(input("enetr your jeca rank:"))
maths=input("do you have maths paper in hs or ug").lower()

try:
    if caste =="general" and percentg <=50:
        raise lessmarks
    if caste !="general" and percentg<=45:
        raise lessmarks
    if maths !="yes":
        raise math
except lessmarks:
    print(" not enough merks u accuired to pursue mca")
except math:
    print("math is must")
        
