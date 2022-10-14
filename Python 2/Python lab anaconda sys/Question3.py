import sys
import csv

def check(n):
    return (int)(n[-1])

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
    result=map(check,rows)
    print(sum(list(result)))