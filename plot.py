from cProfile import label
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba

plt.style.use("fivethirtyeight")

sns.set_theme()
sns.color_palette("bright")

directories = [f'alg{i}' for i in range(1, 6)]
path = ['appendicitis', 'Breast_Cancer_Wisconsin', 'hepatitis', 'indian_liver_patient']
all_data = [0][0]

for x in path:
    all_data = [pd.read_csv(f"D:/C++/Programs/Python/Input/{x}/{dir}/AverageIter1000.csv",on_bad_lines='skip', nrows=100, usecols=[0, 1, 2, 3], header=None) for dir in directories]

    fig, axs = plt.subplots(nrows=2,ncols=2)

    for data_i in all_data:
        sns.kdeplot(np.array(data_i[0]), shade=False, linewidth=2, ax=axs[0][0])
        sns.kdeplot(np.array(data_i[1]), shade=False, linewidth=2, ax=axs[0][1])
        sns.kdeplot(np.array(data_i[2]), shade=False, linewidth=2, ax=axs[1][0])
        sns.kdeplot(np.array(data_i[3]), shade=False, linewidth=2, ax=axs[1][1])

    for data_i, kdeline_i, dir in zip(all_data, axs[0][0].lines, directories):
        mean = data_i[0].mean()
        xs = kdeline_i.get_xdata()
        ys = kdeline_i.get_ydata()
        height = np.interp(mean, xs, ys)
        color = kdeline_i.get_color()
        axs[0][0].vlines(mean, 0, height, color=color, ls=':', lw=3)
        axs[0][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

    for data_i, kdeline_i, dir in zip(all_data, axs[0][1].lines, directories):
        mean = data_i[1].mean()
        xs = kdeline_i.get_xdata()
        ys = kdeline_i.get_ydata()
        height = np.interp(mean, xs, ys)
        color = kdeline_i.get_color()
        axs[0][1].vlines(mean, 0, height, color=color, ls=':', lw=3)
        axs[0][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

    for data_i, kdeline_i, dir in zip(all_data, axs[1][0].lines, directories):
        mean = data_i[2].mean()
        xs = kdeline_i.get_xdata()
        ys = kdeline_i.get_ydata()
        height = np.interp(mean, xs, ys)
        color = kdeline_i.get_color()
        axs[1][0].vlines(mean, 0, height, color=color, ls=':', lw=3 )
        axs[1][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

    for data_i, kdeline_i, dir in zip(all_data, axs[1][1].lines, directories):
        mean = data_i[3].mean()
        xs = kdeline_i.get_xdata()
        ys = kdeline_i.get_ydata()
        height = np.interp(mean, xs, ys)
        color = kdeline_i.get_color()
        axs[1][1].vlines(mean, 0, height, color=color, ls=':', lw=3, label = 'mean')
        axs[1][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

    axs[0][0].set(xlabel = "Accuracy" , ylabel = "Accurarcy-density" )
    axs[0][1].set(xlabel = "Error" , ylabel = "Error-density" )
    axs[1][0].set(xlabel = "Sensitivity" , ylabel = "sensitivity-density" )
    axs[1][1].set(xlabel = "Specificity" , ylabel = "specificity-density" )

    plt.suptitle(x)
    plt.legend()
    plt.show()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# directories = [f'alg{i}' for i in range(1, 6)]
# all_data = [0][0]
# all_data = [pd.read_csv(f"D:/C++/Programs/Python/Input/Breast_Cancer_Wisconsin/{dir}/AverageIter1000.csv",on_bad_lines='skip', nrows=100, usecols=[0, 1, 2, 3], header=None) for dir in directories]

# fig, axs = plt.subplots(nrows=2,ncols=2)

# for data_i in all_data:
#     sns.kdeplot(np.array(data_i[0]), shade=False, linewidth=2, ax=axs[0][0])
#     sns.kdeplot(np.array(data_i[1]), shade=False, linewidth=2, ax=axs[0][1])
#     sns.kdeplot(np.array(data_i[2]), shade=False, linewidth=2, ax=axs[1][0])
#     sns.kdeplot(np.array(data_i[3]), shade=False, linewidth=2, ax=axs[1][1])

# for data_i, kdeline_i, dir in zip(all_data, axs[0][0].lines, directories):
#     mean = data_i[0].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[0][0].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[0][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[0][1].lines, directories):
#     mean = data_i[1].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[0][1].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[0][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[1][0].lines, directories):
#     mean = data_i[2].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[1][0].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[1][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[1][1].lines, directories):
#     mean = data_i[3].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[1][1].vlines(mean, 0, height, color=color, ls=':', lw=3, label = 'mean')
#     axs[1][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# axs[0][0].set(xlabel = "Accuracy" , ylabel = "Accurarcy-density" )
# axs[0][1].set(xlabel = "Error" , ylabel = "Error-density" )
# axs[1][0].set(xlabel = "Sensitivity" , ylabel = "sensitivity-density" )
# axs[1][1].set(xlabel = "Specificity" , ylabel = "specificity-density" )

# plt.suptitle('Breast_Cancer_Wisconsin graph')
# plt.legend()



# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# directories = [f'alg{i}' for i in range(1, 6)]
# all_data = [0][0]
# all_data = [pd.read_csv(f"D:/C++/Programs/Python/Input/hepatitis/{dir}/AverageIter1000.csv",on_bad_lines='skip', nrows=100, usecols=[0, 1, 2, 3], header=None) for dir in directories]

# fig, axs = plt.subplots(nrows=2,ncols=2)

# for data_i in all_data:
#     sns.kdeplot(np.array(data_i[0]), shade=False, linewidth=2, ax=axs[0][0])
#     sns.kdeplot(np.array(data_i[1]), shade=False, linewidth=2, ax=axs[0][1])
#     sns.kdeplot(np.array(data_i[2]), shade=False, linewidth=2, ax=axs[1][0])
#     sns.kdeplot(np.array(data_i[3]), shade=False, linewidth=2, ax=axs[1][1])

# for data_i, kdeline_i, dir in zip(all_data, axs[0][0].lines, directories):
#     mean = data_i[0].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[0][0].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[0][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[0][1].lines, directories):
#     mean = data_i[1].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[0][1].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[0][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[1][0].lines, directories):
#     mean = data_i[2].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[1][0].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[1][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[1][1].lines, directories):
#     mean = data_i[3].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[1][1].vlines(mean, 0, height, color=color, ls=':', lw=3, label = 'mean')
#     axs[1][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# axs[0][0].set(xlabel = "Accuracy" , ylabel = "Accurarcy-density" )
# axs[0][1].set(xlabel = "Error" , ylabel = "Error-density" )
# axs[1][0].set(xlabel = "Sensitivity" , ylabel = "sensitivity-density" )
# axs[1][1].set(xlabel = "Specificity" , ylabel = "specificity-density" )

# plt.suptitle('hepatitis graph')
# plt.legend()


# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# directories = [f'alg{i}' for i in range(1, 6)]
# all_data = [0][0]
# all_data = [pd.read_csv(f"D:/C++/Programs/Python/Input/indian_liver_patient/{dir}/AverageIter1000.csv",on_bad_lines='skip', nrows=100, usecols=[0, 1, 2, 3], header=None) for dir in directories]

# fig, axs = plt.subplots(nrows=2,ncols=2)

# for data_i in all_data:
#     sns.kdeplot(np.array(data_i[0]), shade=False, linewidth=2, ax=axs[0][0])
#     sns.kdeplot(np.array(data_i[1]), shade=False, linewidth=2, ax=axs[0][1])
#     sns.kdeplot(np.array(data_i[2]), shade=False, linewidth=2, ax=axs[1][0])
#     sns.kdeplot(np.array(data_i[3]), shade=False, linewidth=2, ax=axs[1][1])

# for data_i, kdeline_i, dir in zip(all_data, axs[0][0].lines, directories):
#     mean = data_i[0].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[0][0].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[0][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[0][1].lines, directories):
#     mean = data_i[1].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[0][1].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[0][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[1][0].lines, directories):
#     mean = data_i[2].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[1][0].vlines(mean, 0, height, color=color, ls=':', lw=3)
#     axs[1][0].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# for data_i, kdeline_i, dir in zip(all_data, axs[1][1].lines, directories):
#     mean = data_i[3].mean()
#     xs = kdeline_i.get_xdata()
#     ys = kdeline_i.get_ydata()
#     height = np.interp(mean, xs, ys)
#     color = kdeline_i.get_color()
#     axs[1][1].vlines(mean, 0, height, color=color, ls=':', lw=3, label = 'mean')
#     axs[1][1].fill_between(xs, ys, facecolor=to_rgba(color, alpha=0.2), edgecolor=color, lw=2, label=dir)

# axs[0][0].set(xlabel = "Accuracy" , ylabel = "Accurarcy-density" )
# axs[0][1].set(xlabel = "Error" , ylabel = "Error-density" )
# axs[1][0].set(xlabel = "Sensitivity" , ylabel = "sensitivity-density" )
# axs[1][1].set(xlabel = "Specificity" , ylabel = "specificity-density" )

# plt.suptitle('indian_liver_patient graph')
# plt.legend()
# plt.show()

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

