#!/usr/bin/python
# This script is used to generate delta patches from android source code
# useage python patch_generate.py patch_list patch_dir, patch list 
# is the log of repo format-patch, patch dir is the output dir.

import os
import sys
list1=['0','1','2','3','4','5','6','7','8','9']
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
source_dir=os.getcwd()
patch_list=sys.argv[1]
patch_dir=sys.argv[2]
os.chdir(patch_dir)
os.system("rm * -rf")
patch_dir=os.getcwd()
os.chdir(source_dir)

fo=open(patch_list,"r")
i=0
for line in fo.readlines():	
	if line[0] in list2:
		path=line
		path=path.strip('\n')
		print path
		os.chdir(patch_dir)
		os.makedirs(path)
		os.chdir(source_dir)
	elif line[0] in list1:
		i=i+1
		print "haha"
	else:
		os.chdir(path)
		print os.getcwd()
		print i
		os.system("rm *.patch -rf")
		os.system("git format-patch -" + str(i))
		os.system("mv *.patch " + patch_dir  )
		os.chdir(patch_dir)
		os.system("mv *.patch " + path)
		os.chdir(source_dir)
		i=0
		
fo.close()
