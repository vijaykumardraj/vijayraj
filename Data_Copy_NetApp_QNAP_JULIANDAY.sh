#!/bin/bash
echo "To copy data from NetApp to QNAP based on Julian Day"
echo "Usage: data_copy <fromjday> <tojday> "
echo "Note1: fromjday and tojday cannot be empty"
echo "Note1: fromjday and tojday should be integer"
echo "Note3: fromjday shoule be less than or equal to tojday"

n1=$1
n2=$2
if [ -z $1 -o -z $2 ]
then
echo "<fromjday> <tojdya> should be number"
exit
fi
if ! [[ "$n1" =~ ^[+-]?[0-9]+\.?[0-9]*$ ]] || ! [[ "$n2" =~ ^[+-]?[0-9]+\.?[0-9]*$ ]]
#if ! [ $n1=~^[0-9] -o $n2=~^[0-9] ]
then
echo "<fromjday> <tojdya> should be number!!!"
exit
fi

if [ $n1 -ge $n2 ]
then
echo "fromjday should be less than equal to tojday"
fi

while [ $n1 -le $n2 ]
do
echo $n1
rsync -az /dat01_share/SEGDRAW/jday$n1 /QNAP/
n1=$((n1 + 1))
done
