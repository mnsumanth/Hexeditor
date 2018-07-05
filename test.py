from tkinter import *
from tkinter import filedialog
import binascii

root=Tk()
list=[]
input("Press enter to input a file")
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/SUMANTH/Desktop/",title = "Select file")
with open(root.filename, "rb") as file_obj:
	content = file_obj.read()
	b = str(binascii.hexlify(content))
print(b)

print(len(b))

for i in range(0,len(b)-1,2):
	s=(b[i]+b[i+1])
	list.append(s)
print(list)
	