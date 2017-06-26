"""Excerise 1"""
things=["mozzar","cinderella","salmonella"]
for thing in things:
    thing=thing.capitalize()
    print(thing)
print(things)

e2fList=[["dog","chein"],["cat","chat"],["walrus","morse"]]
e2f=dict(e2fList)
print(e2f)
print(e2f["walrus"])
f2e={}
for item,content in e2f.items():
    f2e[content]=item
print(f2e)
print(f2e["chat"])

eSet=set()
for item in e2f.keys():
    eSet.add(item)
print(eSet)