#!/bin/bash
pyside6-rcc ./ui/res_rs.qrc -o ./res_rs_rc.py

list=$(find ./ui -iname "*.ui")
for i in $list
do
  rep=$(echo $i | sed s/ui/compiled/ | sed s/\\.ui/.py/)
  pyside6-uic $i -o $rep
done

echo Done