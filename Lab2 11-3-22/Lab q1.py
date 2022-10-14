def check_email(e):
	flag=0
	x1,x2=e.index('@'),e.index('.')
	if(e.count('@')>1 or e.count('.')>1):
		return 1
	elif((e.index('@')-e.index('.'))>1):
		return 1
	elif (e[x1+1:x2] not in ['gmail','yahoo' ,'rediffmail','hotmail']):
		return 404
	elif(e.index('@')==0):
		return 1
	else:
		return 0
def main():
	s=input("Enter the email you want to check:")
	print("The Entered email is:",s)
	result=check_email(s)
	if(result==0):
		print("Supported email")
	elif(result==404):
		print("Unsupported email")
	else:
		print("Invalid email")
main()
