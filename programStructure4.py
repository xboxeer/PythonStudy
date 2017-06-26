def something():
    print(42)
def run_somthing(method):
    method()
def add_args(*arg):
    print(sum(arg))
def run_something2(method,arg1,arg2):
    method(arg1,arg2)
def edit_story(words,func):
    for word in words:
        print(func(word))
def my_range(first=0, end=10, step=1):
    number=first
    while number<end:
        yield number
        number+=step
run_somthing(something)
run_something2(add_args,2,3)
words=["I","love","xinXin"]
edit_story(words, lambda word: word.capitalize())
print(list(my_range(0,5)))
for x in my_range(0,5):
    print(x)
