#!/bin/bash

n1=10
n2=20
n3=0
echo sum of two number is
n3=$[ $n1 + $n2 ]
echo $n3

echo enter number 1
read n1
echo enter number 2
read n2
sum=$[ $n1 + $n2 ]
echo $sum
op1=add
echo enter operation - add minus multiply divide
read op1
if [ $op1 = "add" ]
then
n3=$[ $n1 + $n2 ]
echo $n3
elif [ $op1 = "minus ]
n3=$[ $n1 - $n2 ]
echo $n3
else
echo you entered other operation
fi


