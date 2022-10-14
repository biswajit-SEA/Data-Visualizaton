s1=str(input("Enter the list separated by comma: "))
l1=s1.split(',')
l2=[]
for i in l1:
	s=""
	for j in i:
		if((j>='a' and j<='z') or (j>='A' and j<='Z')):
			continue
		else:
			s+=(j)
	l2.append(s)
print("Int part of every element of ",l1,"is:",l2)
