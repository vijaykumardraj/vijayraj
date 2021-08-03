#!/usr/bin/python

import sys
a=input()

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



