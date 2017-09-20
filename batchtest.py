import os
from os import listdir
import datetime


for f in listdir("cases"):
    print(f)
    cmd = 'AND.exe cases/'+f
    print( cmd)
    now=datetime.datetime.now()
    os.system(cmd)
    print (datetime.datetime.now()-now)

    
