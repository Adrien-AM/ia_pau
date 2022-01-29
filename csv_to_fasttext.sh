#!/bin/bash

cat $1 | \
    tail -n +2 | \
    cut -d$'\t' -f 2- | \
    sed -e "s/\[]//g" \
	-e "s/.\+\t\(.\+\)\t\(.\+\)$/__label__\2\t\1/" \
