s=str(input("Enter the list separated by comma: "))
l=s.split(',')
print("The list you have entered is:",l)
count=0
for i in l:
	count+=1
print("The number of elements of the list is:",count)
