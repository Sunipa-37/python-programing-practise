graduate=input("qualification ( graduate / undergraduate) :  ").lower()

if graduate == "graduate":
    cast=input(" your  cast (general / sc/ st) :  ").lower()
    if cast!= "general":
        graduation_percent=int(input("your graduatioan marks:"))
        maths_percent=int(input("your maths percentage: "))
        if graduation_percent >=50 and maths_percent>=50:
            print("eligible")
        else:
            print("not eligible")
    else:
        graduation_percent=int(input("your graduatioan marks:"))
        maths_percent=int(input("your maths percentage: "))
        if graduation_percent >=45 and maths_percent>=50:
            print("eligible")
        else:
            print("not eligible")
else:
    print("not eligible")