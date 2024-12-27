#!/bin/bash
list=$(find ./ui -iname "*.ui")
for i in $list
do
  rep=$(echo $i | sed 's/ui/compiled/' | sed 's/\.ui/\.py/')
  pyside6-uic $i -o $rep
done