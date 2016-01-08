# encoding: utf-8  
import os  
import os.path  
# change the filename from oldId to newId in the filenname
curDir = os.getcwd()  
oldId = "[Kamigami] "
newId = ""
for parent, dirnames, filenames in os.walk(curDir):
    for filename in filenames:  
        if filename.find(oldId)!=-1:  
            newName = filename.replace(oldId, newId)  
            print(filename, "---->", newName)  
            os.rename(os.path.join(parent, filename), os.path.join(parent, newName))
os.system("pause")