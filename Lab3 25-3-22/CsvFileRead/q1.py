import sys
import csv

n=len(sys.argv)
number=0
if n!=2:
    print("Enter proper arguments")
else:
    filename=sys.argv[1]
    f=open(filename,'r')
    rows=[]
    csvreader=csv.reader(f)
  
    for line in csvreader:
       if line[0].isnumeric():
           number=number+1
    print(number)