#!/bin/bash
while [[ $# > 1 ]]
do
key="$1"
shift

case $key in
    -f|--first)
    PARAM_FIRST="$1"
    shift
    ;;
    -s|--second)
    PARAM_SECOND="$1"
    shift
    ;;
esac
done
