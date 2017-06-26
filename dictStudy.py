"""dict study"""
emptyDict={}
print(emptyDict)
bierce={1:"Monday",2:"Turesday"}
print(bierce)
lol=[["a","b"],["e","f"],["c","d"]]
lolDict=dict(lol)
lolStr=["ab","cd","ef","gh"]
lolStrDict=dict(lolStr)
print(lol)
print(lolDict)
print(lolStrDict)
lolStrDict["a"]="hahah"
print(lolStrDict)
lolStrDict.update(lolDict)
print(lolStrDict)
del lolStrDict["g"]
print(lolStrDict)
print("a" in lolStrDict)
print(lolStrDict.get("d"))
print(lolStrDict.keys())
print(list(lolStrDict.keys()))
print(lolStrDict.values())
print(lolStrDict.items())
lolStrDict.clear()
print(lolStrDict)
