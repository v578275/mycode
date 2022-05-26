#!/usr/bin/env python3
import shutil
import os

#Change directory
os.chdir('/home/student/mycode/')

#Move file to another directory
shutil.move('raynor.obj', 'ceph_storage/')

#Get new name of file
xname = input('What is the new name for kerrigan.obj? ')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

