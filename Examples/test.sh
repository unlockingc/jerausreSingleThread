#!/bin/bash
./nsaio Coding/coding_matrix to 0x400000000
./nsaio Coding/DataToTransfer to  0x410000000 
sleep 1
./nsaio Coding/DataBack from 0x0 1194584
