import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv(r"cse_grades.csv", index_col=0)
subjects = np.array("M-II CE AP PSP DLD CE-LAB AP-LAB PSP-LAB".split())
grades = np.array("A+ A B C D E F".split())
data = {}
for subject in subjects:
    temp = {}
    for grade in grades:
        temp[grade] = df[df[subject] == grade]["HallTicket-No"].count()
    data[subject] = temp

indexes = np.array([(i, j) for i in range(2) for j in range(4)])


def pie_chart():
    fig, axs = plt.subplots(2, 4)
    for subject, index in zip(subjects, indexes):
        axs[index[0], index[1]].set_title(subject)
        axs[index[0], index[1]].pie(data[subject].values(), labels=data[subject].keys())
    fig.suptitle("Computer Science and Engineering (Semester-2)")
    plt.show()


def line_graph():
    fig = plt.figure()
    for subject in subjects:
        plt.plot(data[subject].keys(), data[subject].values(), label=subject)
    fig.legend(subjects)
    plt.title("Computer Science and Engineering (Semester-2)")
    plt.show()


def bar_graph():
    fig, axs = plt.subplots(2, 4)
    i = 0
    colors = list("bgrcmyk") + ["lime"]
    for subject, index in zip(subjects, indexes):
        axs[index[0], index[1]].set_title(subject)
        axs[index[0], index[1]].bar(data[subject].keys(), data[subject].values(), label=subject, color=colors[i])
        i += 1
    fig.suptitle("Computer Science and Engineering (Semester-2)")
    plt.show()


pie_chart()
line_graph()
bar_graph()
