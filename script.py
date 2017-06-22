#this files combiles 2 text json files into a csv file
#main file for all the script(backbone)


import json
import csv


def dataFinal(data,i):
	final = json.loads(data)
	final_1 = final['restaurants']
	print('finalType',type(final))
	a = final_1[i]
	b = a['restaurant']
	return b

def writeData(dict_data):
	c = list(dict_data.items())
	data = []
	for i in range(0,len(c)):
		data.append(c[i][1])
	return(data)

def writeRows(dict_data):
	c = list(dict_data.items())
	rows = []
	for i in range(0,len(c)):
		rows.append(c[i][0])
	return(rows)

def lib1(data):
	dictDataLib = []
	for i in range(0,20):
		dictDataLib.append(dataFinal(data,i))
	header = writeRows(dictDataLib[0])
	dataFinale = []
	for i in range(0,20):
		dict_data = dictDataLib[i]
		dataFinale.append(writeData(dict_data))
	print('data-type of header and data-finale ', ' ' ,type(header),' ', type(dataFinale))
	return(header,dataFinale)


with open('6.txt','r') as myfile:
	data2 = myfile.read()

with open('7.txt','r') as myfile:
	data3 = myfile.read()


b = lib1(data2)

c = lib1(data3)

header1 = c[0]
dataFinale1 = c[1]
header = b[0]
dataFinale = b[1]


outputFile = open('06.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(header)
for i in range(0,len(dataFinale)):
	outputWriter.writerow(dataFinale[i])
outputFile.close()

outputFile = open('07.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(header1)
for i in range(0,len(dataFinale)):
	outputWriter.writerow(dataFinale1[i])
outputFile.close()

dataFinale12 = dataFinale1 + dataFinale
print(dataFinale12)
print(len(dataFinale12))

outputFile = open('fin.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(header)
for i in range(0,len(dataFinale12)):
	outputWriter.writerow(dataFinale12[i])
outputFile.close()