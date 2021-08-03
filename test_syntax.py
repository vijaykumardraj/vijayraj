#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as myplot
import sys
import random
import time
import tkinter as tk
a=input()
x = []
y = []
def random1():
    x.append(random.randint(1,199))
    y.append(random.randint(1,20))
    print(x)
    print(y)
          
print (not a.isnumeric())

if a.strip() == ("") or not a.isnumeric():
    sys.exit("only number allowed allowed")
if int(a) == 1:
    print(1)
    a
else:
    print("not" + " " +  str(1))
b = ["a"]
a2 = int(a)
while int(a2) <= 10:
    print ("*" * a2)
    b.insert(1,a2)
    a2 += 1
print(b)
for a1 in range(1, 10,2):
    print(a1)

a = [1,2,3,4,5,6]
a.insert(1,15)
print(a)

for i in range(1,20):
    #time.sleep(1)
    random1()
plt.bar(x,y)
plt.show()


x1=[10, 20, 30, 40, 50]
y1=["A", "B", "C", "D", "E"]
myplot.bar(x1,y1)
myplot.show()





