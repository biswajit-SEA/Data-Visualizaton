s1=str(input("Enter the list separated by comma: "))
l1=s1.split(',')
l2=[]
for i in l1:
	if(i not in l2):
		l2.append(i)
print("The list of unique elements is:",l2)
