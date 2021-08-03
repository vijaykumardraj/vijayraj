#!/bin/bash
i=1
while [ $i -lt 10 ]
do
echo $i
i=`expr $i + 1`
done
read a
read b
if [ $a = "a" -a  $b = "b" ]
then
echo value is a or b
else
echo value is no a or b
fi
for i in {1..10}
do
echo $i >> a$i

done

if [ -f a1 ]
then
echo "hello world!" >> a1
fi
read x