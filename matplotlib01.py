import matplotlib.pyplot as myplot
import random
import numpy as np
x=[]
y=[]

for i in range(100):
    x.insert(0, random.randint(1,1000))
    y.insert(0, random.randint(1,1000))
    
myplot.scatter(x,y)
myplot.plot(x,y,'r')
myplot.title("Plot with Random Values")
myplot.xlabel("x-axis")
myplot.ylabel("y-axis")
myplot.savefig("matplotlib01-scatter")
myplot.show()
k=np.arange(10)
l=np.random.uniform(0,10,(8,8))
print(l)
myplot.imshow(l)
#l=np.random.uniform(0,10,10)
#myplot.bar(k,l)
myplot.counter(l)
myplot.savefig("matplotlib01-bar")
myplot.show()

