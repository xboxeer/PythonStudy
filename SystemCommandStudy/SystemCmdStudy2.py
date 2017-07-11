import os
print(os.path.exists('oops.txt'))
print(os.path.abspath('oops.txt'))
os.link('oops.txt','ohno.txt')