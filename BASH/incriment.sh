#!/bin/bash

my_VAR="0"
((my_VAR++))
echo "$my_VAR"
((my_VAR++))
echo "$my_VAR"
((my_VAR++))
echo "$my_VAR"
if [[ $my_VAR -eq "3" ]]; then
    echo "Counter Test Passing; Working as designed."
    exit 0
elif [[ $my_VAR -eq "3" ]]; then
    echo "Counter Failed; Abort!"
    exit 1
fi

