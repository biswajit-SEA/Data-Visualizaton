def fib(a):
	if(a==0 or a==1):
		return (a)
	else:
		return(fib(a-1)+fib(a-2))
a=int(input("Enter the number of terms you want to print of the fibonacci series:"))
for i in range(a):
	b=fib(i)
	print(b,end=" ")
print("\n")
