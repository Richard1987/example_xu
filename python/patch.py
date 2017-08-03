#!/usr/bin/python3
"""
	This script is used to generate delta patch between two manifest
	useage: argv[0] log_file
"""
import os
import sys
import re

if len(sys.argv) < 2:
	print("log_file parameter is needed")
	print(__doc__)
	sys.exit(1)
if sys.argv[1].lower() == "help":
	print(__doc__)
	sys.exit(0)
log_file=sys.argv[1]
source_dir=os.getcwd()
dest_dir=sys.argv[2]
if os.path.isdir(dest_dir):
	os.system(str('rm -rf '+ dest_dir))
os.mkdir(dest_dir)
patch_num=0
pro_path=[]
patch_dest_path=[]
patch_nu=[]
with open(log_file,"r") as f:
	os.chdir(dest_dir)
	for i in f.readlines():
		if re.match(r'[a-zA-Z]',i):
			patch_dest_path.append(i[:len(i)-1])
			os.makedirs(i[:len(i)-1])
			path=os.path.join(source_dir,i)
			pro_path.append(path[0:len(path)-1])
		if re.match(r'[0-9]',i):
			patch_num=patch_num+1
		if i.isspace():
			patch_nu.append(patch_num)
			patch_num=0
print(patch_dest_path)
print(pro_path)
print(patch_nu)

for i in range(len(pro_path)):
	os.chdir(pro_path[i])
	os.system("rm *.patch")
	command1='git format-patch -'+str(patch_nu[i])
	print(pro_path[i])
	os.system(command1)
	final_dir=os.path.join(source_dir,dest_dir,patch_dest_path[i])
	command2='mv *.patch '+final_dir
	os.system(command2)
	


