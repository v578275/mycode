#!/usr/bin/env python3
import shutil
import os

## create file object in "r"ead mode
filename= input("Please provide the filename you want to load:")

with open((filename), "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

lines= os.system("more ~/mycode/cfgread/vlanconfig.cfg | wc -l")
print("The number of lines in the file is: (lines))

