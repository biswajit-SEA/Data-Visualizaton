list_1 = []
list_2 = []
n=int(input("Enter the number of elements in the list:"))
print("Enter the 1st list")
for i in range(0,n):
    a=int(input())
    list_1.append(a)
print("Enter the 2nd list")
for i in range(0,n):
    b=int(input())
    list_2.append(b)
          

list_joined = list_1 + list_2
print(list_joined)
