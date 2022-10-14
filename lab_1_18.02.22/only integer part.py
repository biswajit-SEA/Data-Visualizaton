lis=[]

print("Enter element in the list having both letters and numbers:")
for i in range (5):
    lis.append(input())
print("Only integer part of element of the list:")

for i in lis:
    st=''
    for j in i:
        if j.isdecimal():
            st+=j
    print(st)
