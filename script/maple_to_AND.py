import re
f=open('AMI2048.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('\\\\','',eachline)
    f.writelines(a)
f.close()


f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('\n','',eachline)
    f.writelines(a)
f.close()

f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub(',','\n',eachline)
    f.writelines(a)
f.close()

f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub(' ','',eachline)
    f.writelines(a)
f.close()

f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('A:=','',eachline)
    f.writelines(a)
f.close()

f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('\[' , '',eachline)
    f.writelines(a)
f.close()

f=open('result.txt','r')
alllines=f.readlines()
f.close()
f=open('result.txt','w+')
for eachline in alllines:
    a=re.sub('\]' , '',eachline)
    f.writelines(a)
f.close()