#!/bin/bash

#rsync script - add files to be synced

host=`hostname`

if [ $host == "vm24" ] 
then
echo "----sync-----"
/bin/rsync -az /source/ /target/
else
echo "should run on host: $host"
fi

