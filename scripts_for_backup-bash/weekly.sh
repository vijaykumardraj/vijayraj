#!/bin/bash

tar_count() {
if [ `ls /tar_backup/weekly_*.tar | wc -l` -gt 4 ]
then
oldest_tar_file=`ls -ltr /tar_backup/weekly_*.tar | awk '{print $9}' | head -1`
echo "rm -f $oldest_tar_file"
rm -f $oldest_tar_file
sleep 1
tar_count
fi
}


host=`hostname`
#var1=$(date +%M%H%d%h%y%s_backup)
var1=$(date +%d-%h-%Y-%H-%M-%S-%s_backup)
if [ $host == "vm24" ] 
then
	/usr/bin/tar cf  /tar_backup/weekly_$var1".tar" --absolute-names /target/
	tar_count
else
echo "should run from: $host"
fi

