l=float(input("length: "))
b=float(input("breadth: "))
a= l*b
p=2*(l+b)
if p>a:
    print(" perimeter of the triangle is greater than the area")
else:
    print(" area of the triangle is greater than the perimeter")