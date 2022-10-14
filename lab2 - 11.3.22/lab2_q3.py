#1
import pandas as pd
import sys
import numpy as np
cols=pd.read_csv(sys.argv[1]).columns
file=pd.read_csv(sys.argv[1],usecols=cols[1:8])
if len(sys.argv)==2:
    print("Number of applicants : ", len(file))
else:
    print("enter correct number of command line arguments, i.e, 2")


#6
file["tmarks"]=0

#2
lst = [list(i) for i in file.values]
print("Number of applicants using 2D matrix: ", len(lst))


#3
def selected(l):
    if float(l[-2])==1.0:
        return l
    else:
        return 0


t_lst=list(map(selected,lst))
lst_mod=[]
for i in t_lst:
    if i != 0:
        lst_mod.append(i)
print("Number of selected applicants using map(): ",len(lst_mod))


#4
lst_filtered=list(filter(selected,lst))
print("Number of selected applicants using filter(): ",len(lst_filtered))


#5
columns={}
c_list=list(file.columns)
for i in c_list:
    columns[i]=c_list.index(i)
for key,values in columns.items():
    print(key,":", values)


#6 continued
for i in lst:
    s = 0
    for j in range(1,len(i)-2):
        if np.isnan(i[j]):
            continue
        else:
            s+=i[j]
    i[-1]=s


def select_element(lst):
    return lst[-1]


lst.sort(key=select_element,reverse=True)
OverallM=lst
n_file=pd.DataFrame(lst)
n_file.to_csv("t_marks_sorted.csv")


#7
t20p=int(0.2*len(OverallM))
t60p=int(0.6*len(OverallM))
top20pM,bot40pM=OverallM[0:t20p],OverallM[t60p:]


#8
c=1
def appear(l):
    if not np.isnan(l[c]):
        return l[c]
    else:
        return 'a'


for i in range(1,len(file.columns)-2):
    tot_list,top_list,bot_list=[],[],[]
    t_res=list(map(appear,OverallM))
    t20_res=list(map(appear,top20pM))
    b40_res=list(map(appear,bot40pM))
    for j in t_res:
        if j!='a':
            tot_list.append(j)
    for j in t20_res:
        if j!='a':
            top_list.append(j)
    for j in b40_res:
        if j!='a':
            bot_list.append(j)
    print("Total students appeared in {} : {}".format(file.columns[i],len(tot_list)))
    print("In top 20% {} : {}".format(file.columns[i],len(top_list)))
    print("In bottom 40% {} : {}".format(file.columns[i],len(bot_list)))
    c+=1


#9
def average(l):
    return sum(l)/len(l)


def variance(l):
    com_list = [(i-average(l))**2 for i in l]
    return sum(com_list)/(len(com_list)-1)


def st_dev(l):
    return (variance(l))**0.5


def covar(l1,l2):
    mapped = zip(l1,l2)
    return list(mapped)


def corel(l1,l2):
    corel_list=[i[0]*i[1] for i in covar(l1,l2)]
    return sum(corel_list)/((len(l1)-1)*st_dev(l1)*st_dev(l2))


sorted_file=pd.read_csv("t_marks_sorted.csv")

tmarks_list=sorted_file["7"].tolist()
sel_list=sorted_file["6"].tolist()

tmarks_avg=average(tmarks_list)
sel_avg=average(sel_list)
com_list1,com_list2 = [i-tmarks_avg for i in tmarks_list],[i-sel_avg for i in sel_list]

print("correlation between total marks and final selection : %.5f"%corel(com_list1,com_list2))