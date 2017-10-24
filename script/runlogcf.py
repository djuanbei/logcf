#!/usr/bin/python
import sys
import os
from time import clock
import time

from os import listdir
from os.path import isfile, join


import timelimitexecution

timeout=600 # timeout

def listAllDirectories(path):
    onlyDirectories = [join(path,f) for f in listdir(path) if not isfile(join(path, f))]

    return onlyDirectories


def runOneClassBenchMark(path, LOGCF):
    print path
    fileList=[]
    output=open(path+"/result.csv","w+")
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".txt"):
                fileList.append(os.path.join(root, f))
                
    fileList.sort()
    for fullfilename in fileList:
        print fullfilename
        start=time.time()
        command=LOGCF+"   "+fullfilename
        fileNames=fullfilename.split('/')
        fileName=fileNames[len(fileNames)-1]
        baseName=fileName.split('.')[0]
        
        result=baseName+", >"+str(timeout)+"\n"
        if timelimitexecution.run_with_limited_time(os.system,(command, ),{}, timeout):
            result=baseName+","+str(time.time()-start)+"\n"
        else:
            print "timeout "

        output.write(result)

    output.close()       
    

if __name__ == '__main__':
    if  len(sys.argv)<3:
        exit()

    LOGCF=sys.argv[1]
    inputs=sys.argv[2]
    

    
    DirecList=listAllDirectories(inputs)
    
    for dirs in  DirecList:
        runOneClassBenchMark(dirs, LOGCF)

    
