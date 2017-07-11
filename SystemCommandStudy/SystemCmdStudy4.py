import subprocess
ret=subprocess.getoutput('date')
print(ret)

ret1=subprocess.check_call('date')
print(ret1)
ret2=subprocess.getstatusoutput('date')
print(ret2)
ret3=subprocess.call(['date','-u'])
print(ret3)
ret4=subprocess.call('date -u',shell=True)
print(ret4)