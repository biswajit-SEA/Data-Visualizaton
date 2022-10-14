l=[]
email = input("Enter your email id")
a=0
d=0
f=0
s=""
if((email[0]>'a'and email[0]<'z') or (email[0]>'A' and email[0]<='Z') or (emai[0]>='0' and email[0]<='9')):
    for i in email:
        if i=='@':
            a=a+1
    if a==1:
        l=email.split('@')
        for i in l[0]:
            if (i>='a' and i<='z') or (i>='A' and i<='Z'):
                f=1
                break
        if f:
            if l[1][0]=='.':
                print("invalid")
            else:
                for i in l[1]:
                    if i=='.':
                        d=d+1
                if a>2:
                    print("invalid")
                else:
                    for i in l[1]:
                        if i!='.':
                            s=s+i
                        else:
                            break
                    if (s=="yahoo" or s=="gmail" or s=="rediffmail" or s=="hotmail"):
                        print("valid")
                    else:
                        print("unsupported")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    print("invalid")