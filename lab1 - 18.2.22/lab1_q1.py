lst=input("Enter list elements separated by commas(,): ")
c=0
for i in lst:
    if i==',':
        c+=1
print("Number of elements in the given list: ", c+1)