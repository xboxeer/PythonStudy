from collections import namedtuple
Duck=namedtuple("Duck","bill tail")
duck=Duck("wide orange","long")
print(duck.tail)
print(duck.bill)

parts={"bill":"wide orange","tail":"short"}
duck2=Duck(**parts)
print(duck2.bill)
print(duck2.tail)