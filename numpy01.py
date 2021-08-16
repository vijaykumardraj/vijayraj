import numpy as np
import matplotlib.pyplot as myplot

x=np.linspace(1,90,36000)
y=np.sin(x)
y1=np.cos(x)
y2=np.tan(x)
#myplot.plot(x,y, y1)

myplot.plot(x,y, color="green", label="sin value")
myplot.plot(x,y1, color="blue", label="cos value")

myplot.legend()
myplot.legend()
myplot.title("sin - cos values for 0-180 degrees")
myplot.xlabel("Degrees")
myplot.ylabel("sin - cos function value")
myplot.show()

x=np.random.uniform(0,10,(3,3))

print(x)

