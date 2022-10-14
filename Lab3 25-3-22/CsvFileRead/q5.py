import csv
filename="marks.csv"
fields=[]
rows=[]
d={}
with open(filename,'r')as csvfile:
    csvreader=csv.reader(csvfile)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)
    temp=1
    for i in rows[2]:
        d[temp]=i
        temp+=1
    
    for i,j in d.items():
        print(j,"column","has","index",i)
    
