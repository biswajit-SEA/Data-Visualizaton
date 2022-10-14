import csv
import pandas as pd
def filteredfunction(rowslist):
    for row in rowslist:
        if row[0]=='1':
            return True
        else:
            return False
def main():
    set=[]
    rows=[]
    finalist=[]
    filename='marks.csv'
    results=pd.read_csv(filename)
    with open (filename,"r")as csvfile:
	    csvreader=csv.reader(csvfile)
	    fields=next(csvreader)
	    for row in csvreader:
		    rows.append(row)
	    for row in rows:
		    set.append(row[6])
	    filteredlist=list(map(filteredfunction,set))
	    for a in range(2,len(rows)):
        	    if filteredlist[a]==1:
            		finalist.append(rows[a][0])
	    print("The list of serial no. who are selected",finalist)
	    print("Total number of serial candidate",len(finalist))
main() 

