import random
import math
import sys


print("Guessing Game you should complete in 5 chances")
print ("Enter Your Name")
name = input()
i=random.randint(1,20)

def entry1():
    print("Enter number")
    num = input()
    if not num.isnumeric() or str(num) == "":
        print ("error!!!")
        #entry1()
        sys.exit("wrong input")
    else:
        return(num)


for guess1 in range(4):
    num = entry1()
    print(num)
    if int(num) < i:
        print("too small")
    elif int(num) > i:
        print("too big")
    elif int(num) == i:
        print("your guessed correctly in:" +str(guess1) + " Number is : " + str(i))
        sys.exit("congratulation!!!")
print("wrong guess. better luck next time. Number is: " + str(i))
    
    


    
        
    
