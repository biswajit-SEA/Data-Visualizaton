lst=input("Enter list elements separated by commas: ")
lst1=lst.split(",")
print("Unique elements of the given list are: ")
for i in lst1:
    c=0
    for j in lst1:
        if i==j:
            c+=1
    if c==1:
        print(i)