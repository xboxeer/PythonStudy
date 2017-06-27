class person():
    def __init__(self,name):
        self.name=name
class Doctor(person):
    def __init__(self,name):
        self.name="Doctor:"+name
class Lawyer(person):
    def __init__(self,name):
        self.name="Lawyer:"+name
class EmailPerson(person):
    def __init__(self,name,email):
        super().__init__(name)
        self.email=email

class Duck():
    def __init__(self,inputName):
        self.hiddenName=inputName
    def getName(self):
        print("call getName")
        return self.hiddenName
    def setName(self,name):
        print("call setName")
        self.hiddenName=name
    name=property(getName,setName)