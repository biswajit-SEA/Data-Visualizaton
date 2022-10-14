import csv
import pandas as pd
row1=["201","NA","NA","4","0","0"]
filename="marks.csv"
results=pd.read_csv(filename)
with open(filename,'w') as csvfile:
	csvwriter=csv.writer(csvfile)
	csvwriter.writerow(row1)
print("Number of rows",len(results))
