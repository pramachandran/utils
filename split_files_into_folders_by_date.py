import os
import shutil
import sys
import time
import datetime 

# This script organizes the files from a directory by moving them
# into a specific directory created in PICSYYYYMM format.  
# usage: python (foldername) 
# if a folder name is not specified it will work off the current directory.

if len(sys.argv) > 1:
        folder = sys.argv[1]
else:
        folder = '.'

format = "PICS%Y%m"

print 'Total file: %s' %len(os.walk(folder).next()[2])

for item in os.listdir(folder):

        full_path = os.path.join(folder, item)

	#print "%s" % item + " was last modified: %s" % time.ctime(os.path.getmtime(full_path))
	#print "%s" % item + " was created on: %s" % time.ctime(os.path.getctime(full_path))
	#print "%s" % item + " was added on: %s" % time.ctime(os.path.getatime(full_path))
       
	d = datetime.date.fromtimestamp(os.path.getmtime(full_path))

        if os.path.isdir(full_path):
                continue
       
        dst_folder = os.path.join(folder, d.strftime(format))
       
        if not os.path.exists(dst_folder):
                os.mkdir(dst_folder)
               
        shutil.move(full_path, os.path.join(dst_folder, item))

#Displays file count in sub directory 
for content in os.listdir(folder):
	full_path = os.path.join(folder, content)
	if os.path.isdir(full_path):
		print 'Dir %s' %full_path + ' has : %s' % len(os.walk(full_path).next()[2])

		

