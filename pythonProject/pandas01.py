#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as myplot
import sys
import random
import time
import tkinter as tk

file = 'showpd.xlsx'
x1 = pd.ExcelFile(file)
print(x1.sheet_names)

df1 = x1.parse('Sheet1')
data = pd.read_excel("file1.xlsx")
df = pd.DataFrame(data, columns=['VMName', 'TotalDisk(M)'] )
print (df)
#df.to_excel('file1_test.xlsx')
data.to_csv('file1.csv')
