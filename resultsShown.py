#This is a part of the script.py files that is used to load json data into a dictionary and return data for a particular key
#this was used to sense which of the files had errors while taking in input. Very essential to use it before combine.py as it gave idea that some files had random entries in them(not json ones)
import json
import csv
def resultsShown(data):
	final = json.loads(data)
	n = final['results_shown']
	return n

n = 1216
nResults = []
fileName = []
for i in range(0,n):
	fileName.append(str(i))
for i in range(0,n):
	with open(fileName[i]+'.txt','r',encoding='iso-8859-1') as myfile:
		data = myfile.read()
	nResults.append(resultsShown(data))