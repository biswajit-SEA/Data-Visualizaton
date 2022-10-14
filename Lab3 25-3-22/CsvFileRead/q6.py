import csv
from dataclasses import fields
from importlib.metadata import files
import pandas as pd
rows=[]
df=pd.read_csv('marks.csv')
print(df)
with open('marks.csv', 'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)
    print(rows)
    for i in rows:
        for j in i:
            if(j=='NA'):
                i[i.index(j)]=0
    df['Full_marks']=df['Math']+df['CS']+df['GK']+df['Prog']+df['Comm']
    print(df)
