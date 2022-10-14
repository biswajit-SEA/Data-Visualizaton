import pandas as pd
import matplotlib.pyplot as p
import numpy as np
import seaborn as sns
import csv
sns.set_theme()
count=0
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
with open(r'C:\Users\rajat\Desktop\Input\Input\Breast_Cancer_Wisconsin\alg1\AverageIter1000.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        y1.append(row[3])
with open(r'C:\Users\rajat\Desktop\Input\Input\Breast_Cancer_Wisconsin\alg2\AverageIter1000.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        y2.append(row[3])
with open(r'C:\Users\rajat\Desktop\Input\Input\Breast_Cancer_Wisconsin\alg3\AverageIter1000.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        y3.append(row[3])
with open(r'C:\Users\rajat\Desktop\Input\Input\Breast_Cancer_Wisconsin\alg4\AverageIter1000.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        y4.append(row[3])
with open(r'C:\Users\rajat\Desktop\Input\Input\Breast_Cancer_Wisconsin\alg5\AverageIter1000.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        y5.append(row[3])
Y1a=float(max(y1[0:100]))
Y2a=float(max(y2[0:100]))
Y3a=float(max(y3[0:100]))
Y4a=float(max(y4[0:100]))
Y5a=float(max(y5[0:100]))
Y1b=float(min(y1[0:100]))
Y2b=float(min(y2[0:100]))
Y3b=float(min(y3[0:100]))
Y4b=float(min(y4[0:100]))
Y5b=float(min(y5[0:100]))
Y1c=(Y1a+Y1b)/2
Y2c=(Y2a+Y2b)/2
Y3c=(Y3a+Y3b)/2
Y4c=(Y4a+Y4b)/2
Y5c=(Y5a+Y5b)/2
ya=[Y1a,Y2a,Y3a,Y4a,Y5a]
yb=[Y1b,Y2b,Y3b,Y4b,Y5b]
yc=[Y1c,Y2c,Y3c,Y4c,Y5c]
val=[ya,yb,yc]
#x=['alg1','alg2','alg3','alg4','alg5']
x=np.arange(1,6)
p.bar(x+0.00,val[0],color='cyan',width=0.25,label='max')
p.bar(x+0.25,val[1],color='blue',width=0.25,label='min')
p.bar(x+0.50,val[2],color='green',width=0.25,label='avg')
#p.bar(x,ya,x,yb,x,yc)
p.legend(loc="upper left")
p.xlabel("Algorithm")
p.ylabel("Specificity")
p.show()