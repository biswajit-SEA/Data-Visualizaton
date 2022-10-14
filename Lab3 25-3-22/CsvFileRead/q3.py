import csv
import pandas as pd
def selectionfunction(rowlist):
	for row in rowlist:
		if(row[0]=='1'):
			return 1
		else:
			return 0
def main():
	sel=[]
	rows=[]
	serialnolist=[]
	filename='marks.csv'
	with open (filename,'r') as csvfile:
		csvreader=csv.reader(csvfile)
		fields=next(csvreader)
		for row in csvreader:
			rows.append(row)
		for row in rows:
			sel.append(row[6])
		selectionlist=list(map(selectionfunction,sel))
		for a in range(2,len(rows)):
			if(selectionlist[a]==1):
				serialnolist.append(rows[a][0])
		print("The list of Serial numbers who are selected:",serialnolist)
		count=sum(selectionlist[2:len(selectionlist)])
		print("Total number of selected candidates:",count)
main()
