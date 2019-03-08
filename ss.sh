#!/bin/bash
 
cat ./prototxt/index.txt |while read line
do
cat $line >>model.prototxt
done
