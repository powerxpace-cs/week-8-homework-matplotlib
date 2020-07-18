import matplotlib.pyplot as plot
import numpy

def plotgraphs(listxy,listfunc=None,start=-10,stop=10,title="",xlabel="",ylabel=""):
  figure,axes=plot.subplots()
  x=numpy.linspace(start,stop)
  for y in listxy:
    listx=y[0]
    listy=y[1]
    label=y[2]
    axes.plot(listx,listy,label=label)

  for y in listfunc:
    listx=y[0]
    listy=y[1]
    label=y[2]
    axes.plot(listx(x),listy(x),label=label)

  axes.set_title(title)
  axes.set_xlabel(xlabel)
  axes.set_ylabel(ylabel)
  axes.legend()
  plot.show()

plotgraphs([],[[lambda x: x,lambda x: numpy.sin(x),"sin"],[lambda x: x,lambda x: numpy.cos(x),"cos"]],-10,2,"graph","x","y")
