#this script was use to rename the set of text files numerically

import os
files = os.listdir('.')
#natsort(files)
index= 0
for filename in files:
	os.rename(filename,str(index)+'.txt')
	index = index + 1
