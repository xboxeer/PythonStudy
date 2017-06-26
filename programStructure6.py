animal="rabbit"
def change_global_var():
    animal="wolf"
    print(animal," ",id(animal))
    print("locals",locals())
change_global_var()
print(animal," ",id(animal))
print("global:",globals())