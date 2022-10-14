lst=[]
print("Enter list elements having both numbers and alphabets : ")
for i in range(5):
    lst.append(input())
print("Only integer part of elements of list:")
for i in lst:
    st=""
    for j in i:
        if j.isdecimal():
            st+=j
    print(st,end=',')