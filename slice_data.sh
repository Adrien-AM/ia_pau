#!/bin/bash

CLASSIFIER_PATH="classifier"

if [ $# -ne 3 ]
then
    echo "Usage : ./slice_data.sh data_file %train %test"
    exit 0
fi

tmpfile=$(mktemp)
trap "rm -f $tmpfile" EXIT
len=$(wc -l $1 | cut -d' ' -f 1)
((len_train=len*$2/100))
((len_test=len*$3/100))

cat $1 | shuf > $tmpfile
head -n $len_train $tmpfile > $CLASSIFIER_PATH/train_set
tail -n $len_test $tmpfile > $CLASSIFIER_PATH/test_set
