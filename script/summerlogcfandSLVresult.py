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
    ouput=open(LOGCF+dirname+"/sumresult.csv")
    logReader
    slvReader
    with open(logresult, newline='') as myFile:  
        logReader = csv.reader(myFile)
        
    with open(slvresult, newline='') as myFile:  
        slvReader = csv.reader(myFile)
        
    for   logR in logReader and slvR in  slvReader:
        output.write(logR[0], logG[1], slvR[1])
        
    output.close()
    


if __name__ == '__main__':
                
    if  len(sys.argv)<3:
        print " logcf_result  svl_result"
        exit()
    LOGCG=sys.argv[1]
    SLV=sys.argv[2]

    LOGCFList=listAllDirectories(LOGCG)
    SLVLIST=listAllDirectories(SLV)
    sameLIST=list(set(LOGCFList) & set(SLVLIST))
    for dirname in sameLIST:
        combine(LOGCF, SLV, dirname)
        
    
