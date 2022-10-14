import pandas as pd
import matplotlib.pyplot as mp

path_lst, header_list = [], ["alg1", "alg2", "alg3", "alg4", "alg5", "alg6", "alg7", "measures"]
for i in range(7):
    path_lst.append("C:/Users/HP/Desktop/4th Sem/OOP/Assignment_4/alg{}/alg{}.xls".format(i + 1, i + 1))
file = pd.read_excel(path_lst[0], header=None, usecols=[0])
for i in range(23):
    for j in range(7):
        file[j] = pd.read_excel(path_lst[j], header=None, usecols=[i])
    file["measures"] = [x for x in range(1, 31)]
    file.to_csv("C:/Users/HP/Desktop/4th Sem/OOP/Assignment_4/Question {}.csv".format(i + 1), header=header_list, index=False)
    csv_file = pd.read_csv("C:/Users/HP/Desktop/4th Sem/OOP/Assignment_4/Question {}.csv".format(i + 1))
    mp.rcParams.update({'axes.facecolor': 'white'})
    graph = pd.DataFrame(csv_file, columns=["alg1", "alg2", "alg3", "alg4", "alg5", "alg6", "alg7", "measures"])
    graph.plot(x="measures", y=["alg1", "alg2", "alg3", "alg4", "alg5", "alg6", "alg7"], kind="line", figsize=(90, 90))
    mp.title("Question {} visualisation".format(i + 1))
    mp.xlabel("Number of observations")
    mp.ylabel("Value")
    mp.grid()
    mp.show()
