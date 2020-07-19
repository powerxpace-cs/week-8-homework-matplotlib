import matplotlib.pyplot as plt
import numpy as np


def plotgraphs(listxy,
               listfunc=None,
               start=-10,
               stop=10,
               title="",
               xlabel="",
               ylabel=""):
    # figure, axes = plt.subplots()
    x = np.linspace(start, stop)
    for item in listxy:
        # listx = item[0]
        # listy = item[1]
        # label = item[2]
        plt.plot(item[0], item[1], label=item[2])

    for item in listfunc:
        # listx = item[0]
        # listy = item[1]
        # label = item[2]
        plt.plot(item[0](x), item[1](x), label=item[2])

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()


plotgraphs([[[1, 2, 3, 4], [8, 7, 5, 4], "line segments"], 
            [[1, 2, 3, 4, 5], [1, 4, 9, 16, 25], "square"]],
           [[lambda x: x, lambda x: x**3 - x, "cubic"],
            [lambda x: x, lambda x: x * x, "computed square"],
            [lambda x: np.sin(x), lambda x: np.cos(x), "circle"]], -np.pi, np.pi,
           "graph", "x", "y")
