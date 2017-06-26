"""function/method in python"""
def do_nothing():
    pass
def makeASound():
    print("ahhhh")
def commentary(color):
    if color=="red":
        print("you passed in redf")
    elif color=="black":
        print("you passed in black")
    else:
        print("i don't know what did you pass in")
def commentaryWithReturn(color):
    if color=="red":
        return "you passed in redf"
    elif color=="black":
        return "you passed in black"
    else:
        return "i don't know what did you pass in"
def menu(wine,entree,dessert="pudding"):
    print("we have wine "+wine\
    +" entree:"+entree\
    +" dessert:"+dessert)
def work(arg,result):
    result.append(arg)
    print(result)
def works(arg, result=[]):
    result.append(arg)
    print(result)
def works2(arg):
    result=[]
    result.append(arg)
    print(result)
def works3(arg, result=None):
    if result is None:
        result=[]
    result.append(arg)
    print(result)
def print_args(*args):
    print(args)
def print_kwargs(**kwarg):
    print(kwarg)
def print_myArgs(*args,**kwargs):
    '''
    print all the args
    '''
    print(args)
    print(kwargs)
do_nothing()
makeASound()
commentary("white")
print(commentaryWithReturn("black"))
menu("beer",entree="aaa",dessert="ddd")
menu("beer","aaa")

work("a",[])
work("b",[])

#it appears that if you do not specify the second arg result
#python will init the specific arg result and the next time you call the function
#the arg will reference the original one
works("a")
works("b")
works2("a")
works2("b")
works3("a")
works3("b")
print_args("1",2,3,"aaaa")
print_kwargs(wine="beer",entree="beef")
print_myArgs(1,2,3,wine="beer",entree="beef")
help(print_myArgs)
help(print_myArgs.__doc__)