import matplotlib.pyplot as plt
import numpy as np


def plotlists(listxy):
    for item in listxy:
        plt.plot(item[0], item[1], label=item[2])


def plotfunclists(listfunc=None, start=-10, stop=10):
    x = np.linspace(start, stop)

    for item in listfunc:
        plt.plot(item[0](x), item[1](x), label=item[2])


def plotgraph(title="Graph", xlabel="X", ylabel="Y"):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()


plotlists([[[1, 2, 3, 4], [8, 7, 5, 4], "line segments"],
           [[1, 2, 3, 4, 5], [1, 4, 9, 16, 25], "square"]])
plotfunclists([[lambda x: x, lambda x: x**3 - x, "cubic"],
               [lambda x: x, lambda x: x * x, "computed square"],
               [lambda x: np.sin(x), lambda x: np.cos(x), "circle"]], -np.pi,
              np.pi)
plotgraph("Demo Figure")
