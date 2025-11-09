health=input("your current health condition: (execellent/poor ")
age=int(input("your age: "))
location=input(" where are you from: (city/village)").lower()
gender=input(" your gender: (male/ female)").lower()
policy_amount=int(input("you asking amount for loan: "))

# for first condition:
if health=="execellent" and age<35 and age>25 and location =="city" and gender=="male":
        if policy_amount >=200000:
            print(" not eligible for this insuarance")
        else:
            premium=(policy_amount/1000)*4
#for the second condition
elif health=="execellent" and age<35 and age>25 and location =="city" and gender=="female":
        if policy_amount >=100000:
            print(" not eligible for this insuarance")
        else:
            premium=(policy_amount/1000)*3
#for the third condition
elif health=="poor" and age<35 and age>25 and location =="village" and gender=="male":
        if policy_amount >=10000:
            print(" not eligible for this insuarance")
        else:
            premium=(policy_amount/1000)*6       
else:
    print("not eligible for this insuarance")
