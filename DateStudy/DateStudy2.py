import time
now=time.time()
print(now)
t=time.gmtime(now)
print(t)
fmt="it's %A, %B, %d, %Y, UTC time %I:%M:%S %p"
print(time.strftime(fmt,t))