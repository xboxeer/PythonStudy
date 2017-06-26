"""Set Study"""
emptyDict={}
emptySet=set()
evenNumberSet={0,2,4,6}
print(emptyDict)
print(type(emptyDict))
print(type(emptySet))
print(evenNumberSet)
letter=set("letter")
print(letter)
myDict=dict({"ab","cd","ef"})
print(set(myDict))
drinks={
    'martini':{"vodka","vermouth"},
    'black russian':{"vodka","kahlua"},
    'white russian':{"cream","vodka","kahlua"},
    'manhattan':{'rye',"vermouth","bitters"},
}
print("martini" in drinks)
for name, content in drinks.items():
    if "vodka" in content and not "cream" in content:
        print(name)
print("--------")
for name, content in drinks.items():
    if content & {"vodka", "kahlua"} and not "cream" in content:
        print(name)

bruss=drinks["black russian"]
wruss=drinks["white russian"]

a={1,2}
b={2,3}
print(a | b)
print(a.union(b))
print(a-b | b-a)
print(a ^ b)
print(bruss & wruss)
print(bruss<wruss)
