class pallindrome:
	def __init__(self,n):
		self.n=n
	def check_pallindrome(self):
		if(self.n==self.n[::-1]):
			return self.n
		else:
			if(len(self.n)<=4):
				return(self.n+self.n[(len(self.n)-2)::-1])
			else:
				return 0	
		
def main():
	s=input("Enter the numbers to be checked separated by ',':")
	l=s.split(",")
	for i in range(len(l)):
		obj1=pallindrome(l[i])
		p1=obj1.check_pallindrome()		
		l[i]=p1
	print(l)
main()	
