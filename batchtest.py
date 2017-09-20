import os
from os import listdir
import datetime
import sys

import subprocess



for f in listdir("cases"):
    fsock = open('error.log', 'w')
    sys.stderr = fsock  
    cmd = 'AND.exe cases/'+f
    print( cmd)
    now=datetime.datetime.now()

    r=subprocess.check_output(cmd,shell=False)
    # out=p.stdout.read()
    print ("hhhhhhhhhhhhhhhhhh"+str(r))
    os.system(cmd)

    print (datetime.datetime.now()-now)

    
