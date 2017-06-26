def document_it(func):
    def new_function(*arg, **kwarg):
        print("running function:" ,func.__name__)
        print("positional argument",arg)
        print("keyword arguments",kwarg)
        result=func(*arg,**kwarg)
        print("result",result)
        return result
    return new_function
def squre_it(func):
    def new_function(*arg, **kwarg):
        print("running function:" ,func.__name__)
        result=func(*arg,**kwarg)
        print(result*result)
        return result*result
    return new_function
@document_it
@squre_it
def oldFunc(*arg, **kwarg):
    print(arg)
    print(kwarg)
    return sum(arg)
#myNewFunction=document_it(oldFunc)
#myNewFunction(1,2,3,wine="beer",entree="beef")
oldFunc(1,2,3,wine="beer",entree="beef")
        
