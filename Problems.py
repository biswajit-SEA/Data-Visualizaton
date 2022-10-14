import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")
sns.set_theme()
sns.color_palette("bright")

directories = [f'alg{i}' for i in range(1, 8)]
Problem = [f'Problem {i}' for i in range(1,24)]
all_data = [0][0]
all_data = [pd.read_excel(f"D:/C++/Programs/Python/Assignment_4/{dir}/alg.xls", header=None) for dir in directories]

fig = plt.figure()
ax = plt.subplot(111)


for j in range(0,23):
    for data_i, dir in zip(all_data, directories):
        plt.bar(dir, data_i[j].mean(),align='center', alpha=0.5)

    plt.yscale('symlog', linthresh=1e-100)
    plt.suptitle(Problem[j])
    plt.show()
