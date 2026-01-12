class auth(Exception):
    pass
password="747989"
n=3
while(n>0):
    p2=input("enter password:")
    if(p2== password):
        print("login")
        n=n-1
        break
    else:
        n=n-1
        print("wrong password try again", n,"attempt left")
try:
    p2!=password
    raise auth
except auth:
    print("maximum attempt reached \n your account disabled for next 24 hours")
