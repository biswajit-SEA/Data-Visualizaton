import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data1=pd.read_excel(r"L4 01.04.2022\Assignment_4\alg1\alg1.xls",header = None)
data2=pd.read_excel(r"L4 01.04.2022\Assignment_4\alg2\alg2.xls",header = None)
data3=pd.read_excel(r"L4 01.04.2022\Assignment_4\alg3\alg3.xls",header = None)
data4=pd.read_excel(r"L4 01.04.2022\Assignment_4\alg4\alg4.xls",header = None)
data5=pd.read_excel(r"L4 01.04.2022\Assignment_4\alg5\alg5.xls",header = None)
data6=pd.read_excel(r"L4 01.04.2022\Assignment_4\alg6\alg6.xls",header = None)
data7=pd.read_excel(r"L4 01.04.2022\Assignment_4\alg7\alg7.xls",header = None)
for i in range(0,23):
    ag1 = data1[i].abs()
    mean1 = ag1[i].mean()
    ag2 = data2[i].abs()
    mean2 = ag2[i].mean()
    ag3 = data3[i].abs()
    mean3 = ag3[i].mean()
    ag4 = data4[i].abs()
    mean4 = ag4[i].mean()
    ag5 = data5[i].abs()
    mean5 = ag5[i].mean()
    ag6 = data6[i].abs()
    mean6 = ag6[i].mean()
    ag7 = data7[i].abs()
    mean7 = ag7[i].mean()
    Meano=[mean1,mean2,mean3,mean4,mean5,mean6,mean7]
    Algo=['1','2','3','4','5','6','7']
    plt.bar(Algo,Meano,color=['#800080', '#191970', '#1E90FF', '#00CD00', '#FFFF00','#FF8000','#EE0000'])
    plt.title("Problem {}".format(i+1),color="red",fontweight='bold')
    plt.yscale('log')
    plt.xlabel("Algorithms")
    plt.ylabel("Mean Simulation Results")
    plt.show() 
