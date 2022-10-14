def fibonacci(x):
    if x==1 or x==0:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)

a=int(input("Enter number of elements for the series: "))
print("The fibonacci series is till" ,a ,": ")
for i in range(a):
    print(fibonacci(i),end=" ")