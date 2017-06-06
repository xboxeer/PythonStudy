
"""list test"""
myStr='Na '*4
myStr=myStr.replace('N','h',2)
print(myStr[-1:-10:-1])
print(len(myStr))
myStrList=myStr.split(' ')
print(myStrList)
myNewStr=('oh ' * 4).split(' ')
print(','.join(myNewStr))
print(myNewStr.count('oh'))
print(myStr.ljust(50))