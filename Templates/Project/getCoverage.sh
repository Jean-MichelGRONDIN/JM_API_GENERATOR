#!/bin/bash

if [ $# -ne 1 ]; then
    echo "USAGE: $0 [coverage min]"
    exit 1;
fi

COV_MIN=$1

npm run coverage > logs.txt
if [ `echo $?` -ne 0 ]; then
    echo "Error: unit tests failed"
    exit 1
fi

cat logs.txt
if [ `echo $?` -ne 0 ]; then
    echo "Error: gcovr failed"
    exit 1
fi

COV_ACTUAL=`cat logs.txt | grep tests |cut -d'|' -f 2 | sed 's/ //g'`

echo -n "Expected $COV_MIN% got $COV_ACTUAL% : "

if  (( ${COV_ACTUAL%%.*} <  ${COV_MIN%%.*} )) ; then
    echo "KO"
    exit 1
fi

echo "OK"
exit 0
