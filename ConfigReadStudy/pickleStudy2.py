import pickle
class Tiny():
    def __str__(self):
        return 'Tiny'

obj=Tiny()
print(obj)
pickled=pickle.dumps(obj)
print(pickled)
unpickled=pickle.loads(pickled)
print(unpickled)

