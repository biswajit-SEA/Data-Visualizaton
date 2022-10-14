import pandas as pd
import matplotlib.pyplot as plt
ap1=pd.read_csv(r"L3 25.03.2022\Input\Appendicitis\alg1\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
ap2=pd.read_csv(r"L3 25.03.2022\Input\Appendicitis\alg2\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
ap3=pd.read_csv(r"L3 25.03.2022\Input\Appendicitis\alg3\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
ap4=pd.read_csv(r"L3 25.03.2022\Input\Appendicitis\alg4\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
ap5=pd.read_csv(r"L3 25.03.2022\Input\Appendicitis\alg5\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
mean1apa = ap1[0].mean()
mean2apa = ap2[0].mean()
mean3apa = ap3[0].mean()
mean4apa = ap4[0].mean()
mean5apa = ap5[0].mean()
Meanapa=[mean1apa,mean2apa,mean3apa,mean4apa,mean5apa]
max1apa = ap1[0].max()
max2apa = ap2[0].max()
max3apa = ap3[0].max()
max4apa = ap4[0].max()
max5apa = ap5[0].max()
Maxapa=[max1apa,max2apa,max3apa,max4apa,max5apa]
min1apa = ap1[0].min()
min2apa = ap2[0].min()
min3apa = ap3[0].min()
min4apa = ap4[0].min()
min5apa = ap5[0].min()
Minapa=[min1apa,min2apa,min3apa,min4apa,min5apa]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanapa,
	'Maximum':Maxapa,
	'Minimum':Minapa
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("APPENDICITIS ACCURACY",color="red",fontweight='bold')
plt.ylabel("Accuracy")
plt.xlabel("Algorithms")
plt.ylim(80,90)
plt.xticks(rotation=0)
plt.show() 
mean1ape = ap1[1].mean()
mean2ape = ap2[1].mean()
mean3ape = ap3[1].mean()
mean4ape = ap4[1].mean()
mean5ape = ap5[1].mean()
Meanape=[mean1ape,mean2ape,mean3ape,mean4ape,mean5ape]
max1ape = ap1[1].max()
max2ape = ap2[1].max()
max3ape = ap3[1].max()
max4ape = ap4[1].max()
max5ape = ap5[1].max()
Maxape=[max1ape,max2ape,max3ape,max4ape,max5ape]
min1ape = ap1[1].min()
min2ape = ap2[1].min()
min3ape = ap3[1].min()
min4ape = ap4[1].min()
min5ape = ap5[1].min()
Minape=[min1ape,min2ape,min3ape,min4ape,min5ape]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanape,
	'Maximum':Maxape,
	'Minimum':Minape
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("APPENDICITIS ERROR",color="red",fontweight='bold')
plt.ylabel("Error")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(9,19)
plt.show() 
mean1aps = ap1[2].mean()
mean2aps = ap2[2].mean()
mean3aps = ap3[2].mean()
mean4aps = ap4[2].mean()
mean5aps = ap5[2].mean()
Meanaps=[mean1aps,mean2aps,mean3aps,mean4aps,mean5aps]
max1aps = ap1[2].max()
max2aps = ap2[2].max()
max3aps = ap3[2].max()
max4aps = ap4[2].max()
max5aps = ap5[2].max()
Maxaps=[max1aps,max2aps,max3aps,max4aps,max5aps]
min1aps = ap1[2].min()
min2aps = ap2[2].min()
min3aps = ap3[2].min()
min4aps = ap4[2].min()
min5aps = ap5[2].min()
Minaps=[min1aps,min2aps,min3aps,min4aps,min5aps]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanaps,
	'Maximum':Maxaps,
	'Minimum':Minaps
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("APPENDICITIS SENSITIVITY",color="red",fontweight='bold')
plt.ylabel("Sensitivity")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(0.6,1.1)
plt.show() 
mean1apsp = ap1[1].mean()
mean2apsp = ap2[1].mean()
mean3apsp = ap3[1].mean()
mean4apsp = ap4[1].mean()
mean5apsp = ap5[1].mean()
Meanapsp=[mean1apsp,mean2apsp,mean3apsp,mean4apsp,mean5apsp]
max1apsp = ap1[1].max()
max2apsp = ap2[1].max()
max3apsp = ap3[1].max()
max4apsp = ap4[1].max()
max5apsp = ap5[1].max()
Maxapsp=[max1apsp,max2apsp,max3apsp,max4apsp,max5apsp]
min1apsp = ap1[1].min()
min2apsp = ap2[1].min()
min3apsp = ap3[1].min()
min4apsp = ap4[1].min()
min5apsp = ap5[1].min()
Minapsp=[min1apsp,min2apsp,min3apsp,min4apsp,min5apsp]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanapsp,
	'Maximum':Maxapsp,
	'Minimum':Minapsp
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("APPENDICITIS SPECIFICITY",color="red",fontweight='bold')
plt.ylabel("Specificity")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(9,19)
plt.show() 

bcw1=pd.read_csv(r"L3 25.03.2022\Input\Breast Cancer Wisconsin\alg1\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
bcw2=pd.read_csv(r"L3 25.03.2022\Input\Breast Cancer Wisconsin\alg2\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
bcw3=pd.read_csv(r"L3 25.03.2022\Input\Breast Cancer Wisconsin\alg3\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
bcw4=pd.read_csv(r"L3 25.03.2022\Input\Breast Cancer Wisconsin\alg4\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
bcw5=pd.read_csv(r"L3 25.03.2022\Input\Breast Cancer Wisconsin\alg5\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
mean1bcwa = bcw1[0].mean()
mean2bcwa = bcw2[0].mean()
mean3bcwa = bcw3[0].mean()
mean4bcwa = bcw4[0].mean()
mean5bcwa = bcw5[0].mean()
Meanbcwa=[mean1bcwa,mean2bcwa,mean3bcwa,mean4bcwa,mean5bcwa]
max1bcwa = bcw1[0].max()
max2bcwa = bcw2[0].max()
max3bcwa = bcw3[0].max()
max4bcwa = bcw4[0].max()
max5bcwa = bcw5[0].max()
Maxbcwa=[max1bcwa,max2bcwa,max3bcwa,max4bcwa,max5bcwa]
min1bcwa = bcw1[0].min()
min2bcwa = bcw2[0].min()
min3bcwa = bcw3[0].min()
min4bcwa = bcw4[0].min()
min5bcwa = bcw5[0].min()
Minbcwa=[min1bcwa,min2bcwa,min3bcwa,min4bcwa,min5bcwa]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanbcwa,
	'Maximum':Maxbcwa,
	'Minimum':Minbcwa
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("BREAST CANCER WISCOIN ACCURACY",color="red",fontweight='bold')
plt.ylabel("Accuracy")
plt.xlabel("Algorithms")
plt.ylim(94,100)
plt.xticks(rotation=0)
plt.show() 
mean1bcwe = bcw1[1].mean()
mean2bcwe = bcw2[1].mean()
mean3bcwe = bcw3[1].mean()
mean4bcwe = bcw4[1].mean()
mean5bcwe = bcw5[1].mean()
Meanbcwe=[mean1bcwe,mean2bcwe,mean3bcwe,mean4bcwe,mean5bcwe]
max1bcwe = bcw1[1].max()
max2bcwe = bcw2[1].max()
max3bcwe = bcw3[1].max()
max4bcwe = bcw4[1].max()
max5bcwe = bcw5[1].max()
Maxbcwe=[max1bcwe,max2bcwe,max3bcwe,max4bcwe,max5bcwe]
min1bcwe = bcw1[1].min()
min2bcwe = bcw2[1].min()
min3bcwe = bcw3[1].min()
min4bcwe = bcw4[1].min()
min5bcwe = bcw5[1].min()
Minbcwe=[min1bcwe,min2bcwe,min3bcwe,min4bcwe,min5bcwe]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanbcwe,
	'Maximum':Maxbcwe,
	'Minimum':Minbcwe
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("BREAST CANCER WISCOIN ERROR",color="red",fontweight='bold')
plt.ylabel("Error")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.show() 
mean1bcws = bcw1[2].mean()
mean2bcws = bcw2[2].mean()
mean3bcws = bcw3[2].mean()
mean4bcws = bcw4[2].mean()
mean5bcws = bcw5[2].mean()
Meanbcws=[mean1bcws,mean2bcws,mean3bcws,mean4bcws,mean5bcws]
max1bcws = bcw1[2].max()
max2bcws = bcw2[2].max()
max3bcws = bcw3[2].max()
max4bcws = bcw4[2].max()
max5bcws = bcw5[2].max()
Maxbcws=[max1bcws,max2bcws,max3bcws,max4bcws,max5bcws]
min1bcws = bcw1[2].min()
min2bcws = bcw2[2].min()
min3bcws = bcw3[2].min()
min4bcws = bcw4[2].min()
min5bcws = bcw5[2].min()
Minbcws=[min1bcws,min2bcws,min3bcws,min4bcws,min5bcws]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanbcws,
	'Maximum':Maxbcws,
	'Minimum':Minbcws
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("BREAST CANCER WISCOIN SENSITIVITY",color="red",fontweight='bold')
plt.ylabel("Sensitivity")
plt.xlabel("Algorithms")
plt.ylim(0.9,1)
plt.xticks(rotation=0)
plt.show() 
mean1bcwsp = bcw1[1].mean()
mean2bcwsp = bcw2[1].mean()
mean3bcwsp = bcw3[1].mean()
mean4bcwsp = bcw4[1].mean()
mean5bcwsp = bcw5[1].mean()
Meanbcwsp=[mean1bcwsp,mean2bcwsp,mean3bcwsp,mean4bcwsp,mean5bcwsp]
max1bcwsp = bcw1[1].max()
max2bcwsp = bcw2[1].max()
max3bcwsp = bcw3[1].max()
max4bcwsp = bcw4[1].max()
max5bcwsp = bcw5[1].max()
Maxbcwsp=[max1bcwsp,max2bcwsp,max3bcwsp,max4bcwsp,max5bcwsp]
min1bcwsp = bcw1[1].min()
min2bcwsp = bcw2[1].min()
min3bcwsp = bcw3[1].min()
min4bcwsp = bcw4[1].min()
min5bcwsp = bcw5[1].min()
Minbcwsp=[min1bcwsp,min2bcwsp,min3bcwsp,min4bcwsp,min5bcwsp]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanbcwsp,
	'Maximum':Maxbcwsp,
	'Minimum':Minbcwsp
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("BREAST CANCER WISCOIN SPECIFICITY",color="red",fontweight='bold')
plt.ylabel("Specificity")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.show() 
h1=pd.read_csv(r"L3 25.03.2022\Input\Hepatitis\alg1\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
h2=pd.read_csv(r"L3 25.03.2022\Input\Hepatitis\alg2\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
h3=pd.read_csv(r"L3 25.03.2022\Input\Hepatitis\alg3\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
h4=pd.read_csv(r"L3 25.03.2022\Input\Hepatitis\alg4\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
h5=pd.read_csv(r"L3 25.03.2022\Input\Hepatitis\alg5\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
mean1ha = h1[0].mean()
mean2ha = h2[0].mean()
mean3ha = h3[0].mean()
mean4ha = h4[0].mean()
mean5ha = h5[0].mean()
Meanha=[mean1ha,mean2ha,mean3ha,mean4ha,mean5ha]
max1ha = h1[0].max()
max2ha = h2[0].max()
max3ha = h3[0].max()
max4ha = h4[0].max()
max5ha = h5[0].max()
Maxha=[max1ha,max2ha,max3ha,max4ha,max5ha]
min1ha = h1[0].min()
min2ha = h2[0].min()
min3ha = h3[0].min()
min4ha = h4[0].min()
min5ha = h5[0].min()
Minha=[min1ha,min2ha,min3ha,min4ha,min5ha]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanha,
	'Maximum':Maxha,
	'Minimum':Minha
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("HEPATITIS ACCURACY",color="red",fontweight='bold')
plt.ylabel("Accuracy")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(40,80)
plt.show() 
mean1he = h1[1].mean()
mean2he = h2[1].mean()
mean3he = h3[1].mean()
mean4he = h4[1].mean()
mean5he = h5[1].mean()
Meanhe=[mean1he,mean2he,mean3he,mean4he,mean5he]
max1he = h1[1].max()
max2he = h2[1].max()
max3he = h3[1].max()
max4he = h4[1].max()
max5he = h5[1].max()
Maxhe=[max1he,max2he,max3he,max4he,max5he]
min1he = h1[1].min()
min2he = h2[1].min()
min3he = h3[1].min()
min4he = h4[1].min()
min5he = h5[1].min()
Minhe=[min1he,min2he,min3he,min4he,min5he]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanhe,
	'Maximum':Maxhe,
	'Minimum':Minhe
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("HEPATITIS ERROR",color="red",fontweight='bold')
plt.ylabel("Error")
plt.xlabel("Algorithms")
plt.ylim(0,50)
plt.xticks(rotation=0)
plt.show() 
mean1hs = h1[2].mean()
mean2hs = h2[2].mean()
mean3hs = h3[2].mean()
mean4hs = h4[2].mean()
mean5hs = h5[2].mean()
Meanhs=[mean1hs,mean2hs,mean3hs,mean4hs,mean5hs]
max1hs = h1[2].max()
max2hs = h2[2].max()
max3hs = h3[2].max()
max4hs = h4[2].max()
max5hs = h5[2].max()
Maxhs=[max1hs,max2hs,max3hs,max4hs,max5hs]
min1hs = h1[2].min()
min2hs = h2[2].min()
min3hs = h3[2].min()
min4hs = h4[2].min()
min5hs = h5[2].min()
Minhs=[min1hs,min2hs,min3hs,min4hs,min5hs]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanhs,
	'Maximum':Maxhs,
	'Minimum':Minhs
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("HEPATITIS SENSITIVITY",color="red",fontweight='bold')
plt.ylabel("Sensitivity")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(0,1.2) 
plt.show() 
mean1hsp = h1[1].mean()
mean2hsp = h2[1].mean()
mean3hsp = h3[1].mean()
mean4hsp = h4[1].mean()
mean5hsp = h5[1].mean()
Meanhsp=[mean1hsp,mean2hsp,mean3hsp,mean4hsp,mean5hsp]
max1hsp = h1[1].max()
max2hsp = h2[1].max()
max3hsp = h3[1].max()
max4hsp = h4[1].max()
max5hsp = h5[1].max()
Maxhsp=[max1hsp,max2hsp,max3hsp,max4hsp,max5hsp]
min1hsp = h1[1].min()
min2hsp = h2[1].min()
min3hsp = h3[1].min()
min4hsp = h4[1].min()
min5hsp = h5[1].min()
Minhsp=[min1hsp,min2hsp,min3hsp,min4hsp,min5hsp]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanhsp,
	'Maximum':Maxhsp,
	'Minimum':Minhsp
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("HEPATITIS SPECIFICITY",color="red",fontweight='bold')
plt.ylabel("Specificity")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(0,55)
plt.show() 
l1=pd.read_csv(r"L3 25.03.2022\Input\Indian Liver Patient\alg1\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
l2=pd.read_csv(r"L3 25.03.2022\Input\Indian Liver Patient\alg2\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
l3=pd.read_csv(r"L3 25.03.2022\Input\Indian Liver Patient\alg3\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
l4=pd.read_csv(r"L3 25.03.2022\Input\Indian Liver Patient\alg4\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
l5=pd.read_csv(r"L3 25.03.2022\Input\Indian Liver Patient\alg5\AverageIter1000.csv",header=None, nrows=100,usecols=[0,1,2,3])
mean1la = l1[0].mean()
mean2la = l2[0].mean()
mean3la = l3[0].mean()
mean4la = l4[0].mean()
mean5la = l5[0].mean()
Meanla=[mean1la,mean2la,mean3la,mean4la,mean5la]
max1la = l1[0].max()
max2la = l2[0].max()
max3la = l3[0].max()
max4la = l4[0].max()
max5la = l5[0].max()
Maxla=[max1la,max2la,max3la,max4la,max5la]
min1la = l1[0].min()
min2la = l2[0].min()
min3la = l3[0].min()
min4la = l4[0].min()
min5la = l5[0].min()
Minla=[min1la,min2la,min3la,min4la,min5la]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanla,
	'Maximum':Maxla,
	'Minimum':Minla
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("INDIAN LIVER PATIENT ACCURACY",color="red",fontweight='bold')
plt.ylabel("Accuracy")
plt.xlabel("Algorithms")
plt.ylim(60,75)
plt.xticks(rotation=0)
plt.show() 
mean1le = l1[1].mean()
mean2le = l2[1].mean()
mean3le = l3[1].mean()
mean4le = l4[1].mean()
mean5le = l5[1].mean()
Meanle=[mean1le,mean2le,mean3le,mean4le,mean5le]
max1le = l1[1].max()
max2le = l2[1].max()
max3le = l3[1].max()
max4le = l4[1].max()
max5le = l5[1].max()
Maxle=[max1le,max2le,max3le,max4le,max5le]
min1le = l1[1].min()
min2le = l2[1].min()
min3le = l3[1].min()
min4le = l4[1].min()
min5le = l5[1].min()
Minle=[min1le,min2le,min3le,min4le,min5le]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanle,
	'Maximum':Maxle,
	'Minimum':Minle
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("INDIAN LIVER PATIENT ERROR",color="red",fontweight='bold')
plt.ylabel("Error")
plt.xlabel("Algorithms")
plt.ylim(20,35)
plt.xticks(rotation=0)
plt.show() 
mean1ls = l1[2].mean()
mean2ls = l2[2].mean()
mean3ls = l3[2].mean()
mean4ls = l4[2].mean()
mean5ls = l5[2].mean()
Meanls=[mean1ls,mean2ls,mean3ls,mean4ls,mean5ls]
max1ls = l1[2].max()
max2ls = l2[2].max()
max3ls = l3[2].max()
max4ls = l4[2].max()
max5ls = l5[2].max()
Maxls=[max1ls,max2ls,max3ls,max4ls,max5ls]
min1ls = l1[2].min()
min2ls = l2[2].min()
min3ls = l3[2].min()
min4ls = l4[2].min()
min5ls = l5[2].min()
Minls=[min1ls,min2ls,min3ls,min4ls,min5ls]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanls,
	'Maximum':Maxls,
	'Minimum':Minls
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("INDIAN LIVER PATIENT SENSITIVITY",color="red",fontweight='bold')
plt.ylabel("Sensitivity")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(0.4,0.8)
plt.show() 
mean1lsp = l1[1].mean()
mean2lsp = l2[1].mean()
mean3lsp = l3[1].mean()
mean4lsp = l4[1].mean()
mean5lsp = l5[1].mean()
Meanlsp=[mean1lsp,mean2lsp,mean3lsp,mean4lsp,mean5lsp]
max1lsp = l1[1].max()
max2lsp = l2[1].max()
max3lsp = l3[1].max()
max4lsp = l4[1].max()
max5lsp = l5[1].max()
Maxlsp=[max1lsp,max2lsp,max3lsp,max4lsp,max5lsp]
min1lsp = l1[1].min()
min2lsp = l2[1].min()
min3lsp = l3[1].min()
min4lsp = l4[1].min()
min5lsp = l5[1].min()
Minlsp=[min1lsp,min2lsp,min3lsp,min4lsp,min5lsp]
F=pd.DataFrame({
	'Algo':['1','2','3','4','5'],
	'Mean':Meanlsp,
	'Maximum':Maxlsp,
	'Minimum':Minlsp
})
F.plot(x='Algo',y=['Maximum','Minimum','Mean'], kind="bar",color=["black","yellow","red"])
plt.title("INDIAN LIVER PATIENT SPECIFICITY",color="red",fontweight='bold')
plt.ylabel("Specificity")
plt.xlabel("Algorithms")
plt.xticks(rotation=0)
plt.ylim(20,35)
plt.show() 