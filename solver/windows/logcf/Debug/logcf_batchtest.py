import os
from os import listdir
import datetime
import sys
import time

import subprocess
import xlsxwriter

def haha():
    workbook = xlsxwriter.Workbook("batchtest.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "name")
    worksheet.write(0, 1, "time")
    worksheet.write(0, 2, "root")
    count = 0
    for f in listdir("cases"):
        count += 1
        cmd = 'rootisolate.exe cases/'+f
        print( cmd)
        now=datetime.datetime.now()
        start=time.time()
        r=subprocess.check_output(cmd,shell=False)
        rootnum = str(r).split("\\r\\n")[1].split(" ")[0]
        retime = str(time.time()-start)
        print(rootnum + " "+ retime)
        worksheet.write(count, 0, f)
        worksheet.write(count, 1, retime)
        worksheet.write(count, 2, rootnum)
        #print (r[0:-2].decode())
        #print ("time(s): "+str(time.time()-start)+"\n")
    workbook.close()

    
if __name__ == "__main__":
    haha()