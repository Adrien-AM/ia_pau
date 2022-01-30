#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Usage : ./format_data.sh data_file classification_file"
    exit 0
fi

sort -n  $2 | cut -d$'\t' -f2,3,5 > sorted_classifications.txt

cut -d$'\t' -f2,3,7 $1 > reduced_claims.txt
