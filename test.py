from tkinter import *
from tkinter import filedialog
import binascii
import os

root=Tk()
data=[]
input("Press enter to input a file")
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/SUMANTH/Desktop/",title = "Select file")
with open(root.filename, "rb") as file_obj:
	content = file_obj.read()
	b = str(binascii.hexlify(content))
#print(b)

#print(len(b))

for i in range(0,len(b)-1,2):
	s=(b[i]+b[i+1])
	data.append(s)
del data[0]
#print(len(data))
file=open("file.txt",'w')
for i in range(0,len(data),16):
	#print(len(data))
	#print(i)
	#print(data[i:i+16])
	#file.write(str(data[i:i+16]))
	#file.write('\n\n')
	stop=i+16
	for j in range(i,stop):
		if j<len(data):
			file.write(data[j])
			file.write('\t')
	file.write('\n\n')
		
file.close()
os.system("notepad.exe file.txt")