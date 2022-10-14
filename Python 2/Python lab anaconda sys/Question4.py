import sys
import csv

def check(n):
    if(n[-1]=='1'):
        return True
    else:
        return False
    

n=len(sys.argv)
number=0
if n!=2:
    print("Wrong arguments")
else:
    fname=sys.argv[1]
    f=open(fname,'r')
    rows=[]
    csvreader=csv.reader(f)
  
    for line in csvreader:
       if line[0].isnumeric():
           rows.append(line)
    result=filter(check,rows)
    cnt=0
    for i in result:
        cnt=cnt+1
    print(cnt)