import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1=pd.read_excel(r"D:\4th sem\oops\Assignment_4\Assignment_4\alg1\alg1.xls",header= None)
data2=pd.read_excel(r"D:\4th sem\oops\Assignment_4\Assignment_4\alg2\alg2.xls",header= None)
data3=pd.read_excel(r"D:\4th sem\oops\Assignment_4\Assignment_4\alg3\alg3.xls",header= None)
data4=pd.read_excel(r"D:\4th sem\oops\Assignment_4\Assignment_4\alg4\alg4.xls",header= None)
data5=pd.read_excel(r"D:\4th sem\oops\Assignment_4\Assignment_4\alg5\alg5.xls",header= None)
data6=pd.read_excel(r"D:\4th sem\oops\Assignment_4\Assignment_4\alg6\alg6.xls",header= None)
data7=pd.read_excel(r"D:\4th sem\oops\Assignment_4\Assignment_4\alg7\alg7.xls",header= None)

for i in range(0,22):
    a1=data1[i].abs()
    mean1=a1.mean()
    a2=data2[i].abs()
    mean2=a2.mean()
    a3=data3[i].abs()
    mean3=a3.mean()
    a4=data4[i].abs()
    mean4=a4.mean()
    a5=data5[i].abs()
    mean5=a5.mean()
    a6=data5[i].abs()
    mean6=a6.mean()
    a7=data7[i].abs()
    mean7=a7.mean()

    Algorithm=['Alg1','Alg2','Alg3','Alg4','Alg5','Alg6','Alg7']
    Mean=[mean1,mean2,mean3,mean4,mean5,mean6,mean7]

    plt.bar(Algorithm,Mean,width=0.3,color='Olive')
    plt.yscale('Log')
    plt.xlabel('Algorithm')
    plt.ylabel('Mean')
    plt.title('Problem'+ str(i + 1))
    plt.show()