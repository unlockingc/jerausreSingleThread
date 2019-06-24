#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from os import listdir
from os.path import isfile, join, getsize
from numpy import *
import os

parser = argparse.ArgumentParser()
parser.add_argument('filePrefix')
args = parser.parse_args()

if __name__=='__main__':
    # print(args)
    print("====Data prefix is: {}====\n".format(args.filePrefix))
    onlyfiles = [f for f in listdir("Coding") if isfile(join("Coding", f))]
    onlyfiles = sorted(onlyfiles)
    # print(onlyfiles)

    files = []
    for f in onlyfiles:
        if f.startswith(args.filePrefix) and not ("meta" in f) and not ("decoded" in f):
            print( "adding {}\n".format(f) )
            fo = open( join("Coding", f), "rb" )
            files.append(fo)
    fout = open( join("Coding", "DataToTransfer"), "wb" )

    end = False
    chunk = 32
    #suffix  = '0' - '0'
    #print("suffix length: {}".format(len(suffix)))
    while not end:
        for f in files:
            temp = f.read(chunk)
            if len(temp) == chunk:
                fout.write(temp)
            elif len(temp) > 0:
                print( "in len {} and add {}\n".format(len(temp),chunk-len(temp)) )
                fout.write(temp)
                fout.write(bytes(chunk-len(temp)))
                end = True
            # print("read {} bytes from file {}\n".format(len(temp), f.name))
            else:
                end = True
                break     

    for f in files:
        f.close()
    fout.close()

    dataSize = getsize(join("Coding", "DataToTransfer"))
    print("datasize: {}\n".format(dataSize))

    #redo the matrix
    mf = open( join("Coding", "coding_matrix.txt"), "r" )
    dmf = open( join("Coding", "decoding_matrix.txt"), "r" )

    mfb = open( join("Coding", "coding_matrix"), "wb" )
    dmfb = open( join("Coding", "decoding_matrix"), "wb" )
    
    temp = mf.read()
    mat = temp.split()

    temp = dmf.read()
    dmat = temp.split()
    
    k = uint8(mat[0])
    m = uint8(mat[1])
    print(k)

    mfb.write(m)
    mfb.write(k)
    mfb.write(bytes(8-2))
    print("dataSize: {}".format(dataSize))
    mfb.write(int64(dataSize))
    mfb.write(bytes(32-8-8))

    dmfb.write(m)
    dmfb.write(k)
    dmfb.write(bytes(8-2))
    dmfb.write(int64(dataSize))
    dmfb.write(bytes(32-8-8))

    for i in range(0,m):
        for j in range(0, k):
            mfb.write(uint8(mat[i*k + j + 2]))
            dmfb.write(uint8(dmat[i*k + j + 2]))
        mfb.write(bytes(32-k))
        dmfb.write(bytes(32-k))
    mf.close()
    dmf.close()
    mfb.close()
    dmfb.close()
    #print(size(k))
    