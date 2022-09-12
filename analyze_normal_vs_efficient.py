from copy import deepcopy
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def drawsubfigure(ax: Axes, list_title: list, list_runtime: list):
    size = 2 ** np.arange(1, len(list_runtime[0]) + 1)
    plt_legends = []
    plt_title = ""
    for title, runtime in zip(list_title, list_runtime):
        model, num_threads, num_rounds, num_lines, pipes, *args = title.split()
        ax.plot(size, runtime)
        plt_title = pipes
        plt_legends.append(model)
    ax.set_title(plt_title)
    ax.set_xlabel("size")
    ax.set_ylabel("runtime")
    ax.legend(plt_legends, loc="best")
    return

def drawfigure(list_title: list, list_runtime: list):
    fig, ax = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True)

    pipes = ["ssss", "spsp", "sppp", "ssssssss", "spspspsp", "sppppppp", "ssssssssssssssss", "spspspspspspspsp", "sppppppppppppppp"]
    for j in range(len(pipes)):
        list_title_jp, list_runtime_jp = [], []
        for i in range(len(list_title)):
            title = list_title[i].split()
            p = title[4][6:]
            if p == pipes[j]:
                list_title_jp.append(list_title[i])
                list_runtime_jp.append(list_runtime[i])
        drawsubfigure(ax[j // 3, j % 3], list_title_jp, list_runtime_jp)

    plt.suptitle(list_title[0].split()[1] + "  " + list_title[0].split()[3])
    plt.tight_layout()
    plt.show()

def draw(list_title: list, list_runtime: list):
    num_threads = [4, 8, 16, 24]

    for j in num_threads:
        list_title_jt, list_runtime_jt = [], []
        for i in range(len(list_title)):
            title = list_title[i].split()
            n = int(title[1][12:])
            if n == j:
                list_title_jt.append(list_title[i])
                list_runtime_jt.append(list_runtime[i])
        drawfigure(list_title_jt, list_runtime_jt)


def process(file: str):
    with open(file) as f:
        lines = f.readlines()

    title = ""
    runtime = []

    list_title, list_runtime = [], []

    for line in lines:
        if line[0:5] == "model":
            if title != "":
                list_title.append(title)
                list_runtime.append(deepcopy(runtime))
            title = line[:-1]
            runtime.clear()
        elif line != "":
            s, r = line.split()
            if s == "size":
                continue
            runtime.append(float(r))

    list_title.append(title)
    list_runtime.append(deepcopy(runtime))
    return list_title, list_runtime

datatype = sys.argv[1]

path = "D:\second_year_2\gsoc\\normal_vs_efficient_" + datatype
files = os.listdir(path)
list_title, list_runtime = [], []

for f in files:
    titles, runtimes = process(path + '\\' + f)
    list_title.extend(titles)
    list_runtime.extend(runtimes)

draw(list_title, list_runtime)

