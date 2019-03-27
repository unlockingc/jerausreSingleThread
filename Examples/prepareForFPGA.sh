#! /bin/bash
if [ ! -d "DeletePart" ]; then
  mkdir DeletePart
fi

rm DeletePart/*

if [ -d "Coding" ]; then
  rm Coding -r
fi

k=$2
m=$3
dataPrefix=$1
partToDelete1=$4
partToDelete2=$5

./encoder $1 $2 $3 reed_sol_van 8 0 0

mv Coding/${dataPrefix}_${partToDelete1} DeletePart/
mv Coding/${dataPrefix}_${partToDelete2} DeletePart/

./decoder $1
./dataPreprocess.py ${dataPrefix}