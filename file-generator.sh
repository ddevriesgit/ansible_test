#!/bin/bash
# Generate a dummy file of decent size for some data-transfer testing
# Inteded to be used as part of a cronjob
# Derek DeVries 19 October 2021



time=`date +RR`
date=`date +%F`

big_dir=~/projects/mock-RCS/VIP_fakedata/

if [ ! -d $big_dir/Confocal_$date ]
then
	mkdir $bigdir/Confocal_$date
fi


file=$big_dir/Confocal_$date/recording-$time
touch $file

dd if=/dev/zero of=$file bs=1000 count=1000

