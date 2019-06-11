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
    
    filename = ""
    with open(filename, "r" ) as f:
        with open(filename+"_bin", "wb") as fo:
            temp = f.read()
            fo.write(bytes(temp))
