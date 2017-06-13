#! /bin/bash
# -*- coding: utf8 -*-

PWD=`pwd`
LOG_FILE=$PWD/testing.log

compile_pass ()
{
    ./figures_smath.py --all --pass-number=$1 &&
    pytex lst_smath.py --no-external 
}

# Remove the garbage files

rm *.pyc >> /dev/null
rm *.pstricks 
rm tikz*.md5 >> /dev/null
rm tikz*.pdf >> /dev/null
rm *.aux >> /dev/null

compile_pass 1 &&
compile_pass 2 &&
#compile_pass 3 

./test_recall.py . >> $LOG_FILE

echo "----------------------"
echo "Results in " $LOG_FILE

cat $LOG_FILE

echo "-----------------------"

