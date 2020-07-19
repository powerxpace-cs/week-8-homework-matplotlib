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
    for y in listxy:
        listx = y[0]
        listy = y[1]
        label = y[2]
        plt.plot(listx, listy, label=label)

    for y in listfunc:
        listx = y[0]
        listy = y[1]
        label = y[2]
        plt.plot(listx(x), listy(x), label=label)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()


plotgraphs([[[1, 2, 3, 4], [8, 7, 5, 4], ""]],
           [[lambda x: x, lambda x: x**3 - x, "cubic"],
            [lambda x: np.sin(x), lambda x: np.cos(x), "circle"]], -3.14, 3.14,
           "graph", "x", "y")
