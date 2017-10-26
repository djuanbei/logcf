#!/usr/bin/python
import sys
import os
import csv
from time import clock
import time

from os import listdir
from os.path import isfile, join


def combine(LOGCF, SLV, dirname):

    logresult=LOGCF+dirname+"/result.csv"
    
    slvresult=SLV+dirname+"/result.csv"
    output=open(LOGCF+dirname+"/sumresult.csv","w+")
    print dirname    
    logReader=csv.reader(open(logresult, 'r'))
    slvReader=csv.reader(open(slvresult, 'r'))
    logData=[]
    slvData=[]
    for logR in logReader:
        logData.append(logR)
    for slvR in slvReader:
        slvData.append(slvR);

    for i in range(len(logData)):

        output.write(logData[i][0]+","+ logData[i][1]+","+ slvData[i][1]+"\n")

        
    output.close()
    
def listAllDirectories(path):
    onlyDirectories = [f for f in listdir(path) if not isfile(join(path, f))]

    return onlyDirectories

if __name__ == '__main__':
                
    if  len(sys.argv)<3:
        print " logcf_result  svl_result"
        exit()
    LOGCF=sys.argv[1]
    SLV=sys.argv[2]

    LOGCFList=listAllDirectories(LOGCF)
    SLVLIST=listAllDirectories(SLV)
    print LOGCFList
    print SLVLIST
    sameLIST=list(set(LOGCFList) & set(SLVLIST))

    for dirname in sameLIST:
        combine(LOGCF, SLV, dirname)
        
    
