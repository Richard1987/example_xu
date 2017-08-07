#!/usr/bin/python3
"""
	This script is used to get commit message from gerrit server
"""
import os
import sys
import subprocess
import json

def get_message(argv):
	command="ssh -p 29418 jenkins@192.168.41.128 gerrit query {0} --commit-message --format JSON | grep commitMessage".format(argv)
	message=subprocess.getoutput(command)
	d1=json.loads(message)

	print(d1['commitMessage'])

	with open('message.log','w') as f:
		f.writelines(d1['commitMessage'])
	return d1
#if len(sys.argv[1:]) 

if __name__ == "__main__":
	print(get_message(sys.argv[1]))


