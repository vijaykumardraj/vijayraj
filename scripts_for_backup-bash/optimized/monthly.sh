#!/bin/bash

tar_count() {
if [ `ls /tar_backup/monthly_*.tar | wc -l` -gt 12 ]
then
oldest_tar_file=`ls -ltr /tar_backup/monthly_*.tar | awk '{print $9}' | head -1`
echo "rm -f $oldest_tar_file"
rm -f $oldest_tar_file
sleep 1
tar_count
fi
}


host=`hostname`
#var1=$(date +%M%H%d%h%y%s_backup)
var1=$(date +%d-%h-%Y-%H-%M-%S_backup)
if [ $host == "vm24" ] 
then
weekly_oldest_file=`ls -ltr /tar_backup/weekly_*.tar | awk '{print $9}' | head -1`
mv $weekly_oldest_file  /tar_backup/monthly_$var1".tar"
#	/usr/bin/tar cf  /tar_backup/monthly_$var1".tar" --absolute-names /target/
	tar_count
else
echo "false"
fi

