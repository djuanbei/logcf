import re
import os

basedir = os.path.dirname(os.path.abspath(__file__))
dirname = os.path.join(basedir, "input")

output = os.path.join(basedir, "output")
if(os.path.exists(output) == False):
    os.mkdir(output)
for root, dirs, filename in os.walk(dirname):
    for file in filename:
        if os.path.splitext(file)[1] == '.txt':
            f = open(dirname + "\\" + file, 'r')
            r = open(output +  "\\" + os.path.splitext(file)[0] + "_result.txt", 'w')
            allines=f.readlines()
            for eachline in allines:
                a = re.sub('\n', '', eachline)
                r.writelines(a)
            r.close()
            f.close()