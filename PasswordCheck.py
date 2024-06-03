def basic():
    p = input("Your password")
    if p.isalpha()==True:
        print("Put numbers")
    elif p.isdecimal()==True:
        print("Put letters")
    elif p.isspace()==True:
        print("Put letters and numbers")
    elif p.isalnum()==True:
        print("Password accepted")
    else:
        print("Stop,you are not slick")

def detailed():
    p = input("Your password")
    fn=0 #number
    fc=0 #capital letter
    fm=0 #lenght
    fl=0 #lowercase letter
    if len(p)>=8:
        fm=1
    for i in range(0,len(p)):
        if p[i].isupper()==True:
            fc=1
    for i in range(0,len(p)):
        if p[i].islower()==True:
            fl=1
    for i in range(0,len(p)):
        if p[i].isdecimal()==True:
            fn=1
    if fn==1 and fl==1 and fc==1 and fm==1:
        print("Your password is secure")
    elif fm==0:
        print("Your password needs to be 8 or more characters")
    elif fn==0:
        print("Your password needs a number")
    elif fl==0:
        print("Your password needs a lowercase letter")
    elif fc==0:
        print("Your password needs a capital letter")