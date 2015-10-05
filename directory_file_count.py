import os
import shutil
import sys
import time
import datetime 

# This script does the count of the files per directory
# usage: python (folderName)

if len(sys.argv) > 1:
        folder = sys.argv[1]
else:
        folder = '.'

for content in os.listdir(folder):
	full_path = os.path.join(folder, content)
	if os.path.isdir(full_path):
		print 'Dir %s' %full_path + ' has : %s' % len(os.walk(full_path).next()[2])

		

