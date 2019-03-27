#! /bin/bash
if [ ! -d "DeletePart" ]; then
  mkdir DeletePart
fi

k=$2
m=$3
dataPrefix=$1
partToDelete1=$4
partToDelete2=$5
./encoder_single $1 $2 $3 reed_sol_van 8 0 0

mv Coding/${dataPrefix}_${partToDelete1}.txt DeletePart/
mv Coding/${dataPrefix}_${partToDelete2}.txt DeletePart/

./decoder_single $1
./dataPreprocess.py dataPrefix