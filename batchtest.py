import os
from os import listdir
import datetime
import subprocess
import commands

for f in listdir("cases"):
    print(f)
    cmd = 'AND.exe cases/'+f
    print( cmd)
    now=datetime.datetime.now()
    status, output = commands.getstatusoutput(cmd)
    print(output)
    # p=subprocess.Popen([cmd],stdout=subprocess.PIPE)
    # out=p.stdout.read()
    # os.system(cmd)
    print (datetime.datetime.now()-now)

    
