#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Usage : ./csv_to_fasttext.sh csvfile fasttext_formatted_file"
    exit 1
fi

cat $1 | \
    tail -n +2 | \
    cut -d$'\t' -f 2- | \
    sed	-e "s/.\+\t\(.\+\)\t\(.\+\)$/\2\t\1/" | \
    sed -e "s/'\(...\).*-.\+',/__label__\1/g" | \
    sed -e "s/'\(...\).*-.\+'\]/__label__\1/g" | \
    sed -e "s/\[//g" > $2


