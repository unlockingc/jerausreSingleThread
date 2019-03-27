#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from os import listdir
from os.path import isfile, join

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
    fout = open( join("Coding", "DataToTransfer.txt"), "wb" )

    end = False
    while not end:
        for f in files:
            temp = f.read(32)
            # print("read {} bytes from file {}\n".format(len(temp), f.name))
            if temp == '' or len(temp) == 0:
                end = True
                break
            else:
                fout.write(temp)

    for f in files:
        f.close()
    fout.close()

