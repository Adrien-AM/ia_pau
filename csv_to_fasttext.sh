#!/bin/bash

((TIME_PER_LINE=12)) # percent

if [ $# -ne 3 ]
then
    echo "Usage : ./format_data.sh data_file classes_file output_file."
    exit 0
fi
tmpfile=$(mktemp)

trap "rm -f $tmpfile" EXIT

echo -n "Creating temporary file from claims ..."

# File for an easier format : ID LANG TEXT , separator is tab
cat $1 | sed -e "/<claim num=/d" -e "s|EP\t\([0-9]*\s..\)\t....-..-..\t\(..\)\tCLAIM\t<claim id=\".*\"\snum=\"[0-9]*\">|\1\t\2\t|g" -e "s|</*claim-text>||g" -e "s|</claim>||g" > $tmpfile

echo "" > $3

echo -e "\tDone.\nNow writing to output. This is gonna take some time."

# Compute estimated time. TIME_PER_LINE is arbitrary and will vary depending on computers.
size=$(wc -l $tmpfile | cut -d' ' -f 1)
((total=size*$TIME_PER_LINE / 100))
((sec=total%60))
((min=(total%3600)/60))
((hour=total/3600))

echo 'Estimated time : '$hour'h '$min'm '$sec's.'  

# Associating ID with classes and writing it to output file
while IFS= read -r line
do
    id=$(echo $line | cut -d' ' -f 1)
    text=$(echo $line | cut -d' ' -f 4- | sed -e "s|<.*>||g" -e "s|([0-9]*)||g" -e "s/\r//g")
    classes=$(grep $id $2 | cut -d$'\t' -f 5 | sed -e "s/\(...\).\+/\1/g" -e "s/[\r\n]//g" | sort | uniq)
    for c in $classes
    do
	echo -n "__label__$c " >> $3
    done
    echo -e "\t$text" >> $3
done < $tmpfile


