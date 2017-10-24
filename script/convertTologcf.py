#!/usr/bin/python
import sys
import os

if __name__ == '__main__':
    if  len(sys.argv)<3:
        exit()
    
    source=sys.argv[1]
    target=sys.argv[2]
    fileList=[]
    
    for root, dirs, files in os.walk(source):
        for f in files:
            if f.endswith(".txt"):
                fileList.append(os.path.join(root, f))

                
    for fullfilename in fileList:

        print fullfilename
        
        with open(fullfilename) as f:
            
            filename=fullfilename.replace(source,target).split('.')[0]
            output=filename+".txt"
            directory = os.path.dirname(output)
            try:
                os.stat(directory)
            except:
                os.mkdir(directory)       

            with open(output,"w+") as f1:
                atext= f.read().replace('\n',' ')
                atext= atext.replace('\n',' ')
                atext= atext.replace('\r',' ')
                atext=atext.replace("  "," ")
                atext=atext.replace("  "," ")
                atext=atext.replace("  "," ")
                f1.write(atext)
                f1.close()
            f.close()

