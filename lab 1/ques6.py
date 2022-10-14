s=str(input("Enter the list separated by comma"))
m=s.split(",")
n=[]
for i in n:
    s=" "
    for j in i:
        if((j>='a' and j<='z') or (j>='A' or j<='Z')):
            continue
        else:
            st=str(j)
    n.append(st)

print(n)