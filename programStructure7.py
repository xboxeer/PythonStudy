myList=[1,2,3]
position=6
try:
    myList[position]
except IndexError as error:
    print("error!")
    print(error)
