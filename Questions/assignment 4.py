import pandas as pd
import matplotlib.pyplot as mp
path_list, header_list = [], ["alg1", "alg2", "alg3", "alg4", "alg5", "alg6", "alg7", "measures"]
for i in range(7):
    path_list.append("D:/Documents/notes and syllabus/4th sem"
                     "/Assignments/OOP2 Lab/Assignment_4"
                     "/alg{}/alg{}.xls".format(i + 1, i + 1))
file = pd.read_excel(path_list[0], header=None, usecols=[0])
for i in range(23):
    for j in range(7):
        file[j] = pd.read_excel(path_list[j], header=None, usecols=[i])
    file["measures"] = [x for x in range(1, 31)]
    print(type(file))
    file.to_excel("D:/Documents/notes and syllabus/4th sem/Assignments/OOP2 Lab/Assignment_4"
                  "/Question {}.xls".format(i + 1), header=header_list, index=False)
    excel_file = pd.read_excel("D:/Documents/notes and syllabus/4th sem"
                               "/Assignments/OOP2 Lab/Assignment_4/Question {}.xls".format(i + 1))
    mp.rcParams.update({'axes.facecolor': 'wheat'})
    graph = pd.DataFrame(excel_file, columns=header_list)
    graph.plot(x="measures", y=[header_list[i] for i in range(7)], kind="line", figsize=(50, 50))
    mp.title("Question {} visualisation".format(i + 1))
    mp.xlabel("Number of observations")
    mp.ylabel("Value")
    mp.grid()
    mp.show()
