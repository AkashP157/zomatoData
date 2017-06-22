#this script is to check how can diffrent files of serial names be imported in python and be saved into a text file

n = 1216
fileName = []
for i in range(0,n):
	fileName.append(str(i))
print(fileName)
print(type(fileName[12]))

with open(fileName[12]+'.txt','r') as myfile:
	data = myfile.read()
print(data)
print(type(data))
