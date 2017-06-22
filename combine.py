import json
import csv

def dataFinal(data,i):								#seperates a restaurant key file from data
	final = json.loads(data)
	final_1 = final['restaurants']
	print('finalType',type(final))
	a = final_1[i]
	b = a['restaurant']
	return b

def resultsShown(data):							#gives the number of results in a given file
	final = json.loads(data)
	n = final['results_shown']
	return n

def writeData(dict_data):						#gives the data of file
	c = list(dict_data.items())
	data = []
	for i in range(0,len(c)):
		data.append(c[i][1])
	return(data)

def writeRows(dict_data):						#gives the rows of file
	c = list(dict_data.items())
	rows = []
	for i in range(0,len(c)):
		rows.append(c[i][0])
	return(rows)

def lib1(data):									#final function
	dictDataLib = []
	nResults = resultsShown(data)
	if(nResults == 0):
		pass
	else:
		for i in range(0,nResults):
			dictDataLib.append(dataFinal(data,i))
		header = writeRows(dictDataLib[0])
		dataFinale = []
		for i in range(0,nResults):
			dict_data = dictDataLib[i]
			dataFinale.append(writeData(dict_data))
		print('data-type of header and dataFinale ', ' ' ,type(header),' ', type(dataFinale))
		return(header,dataFinale)


header = []
dataFinale = []

with open('1.txt','r') as myfile:
	dataZero = myfile.read()
a = lib1(dataZero)
header = a[0]

#n = total number of text files
n = 1216
fileName = []
#For a given text file, this loop runs it through the lib function and updates the dataFianle object
for i in range(0,n):
	fileName.append(str(i))
#lines 63,64 standard way to import a text files into a string 
for i in range(0,n):
	with open(fileName[i]+'.txt','r',encoding='iso-8859-1') as myfile: 					#encoding of the text files provided was iso-8859-1 so it has to be added
		data = myfile.read()
	print(fileName[i])
	if(resultsShown(data) == 0):
		pass
	else:	
		b = lib1(data)
		dataFinale = dataFinale + b[1]
print(len(dataFinale))

outputFile = open('finale.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(header)
for i in range(0,len(dataFinale)):
	outputWriter.writerow(dataFinale[i])
outputFile.close()

