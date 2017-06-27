class myClass():
    count=0
    def __init__(self):
        myClass.count+=1
    @classmethod
    def getCount(cls):
        print(cls.count)
class Quote():
    def __init__(self,person,words):
        self.person=person
        self.words=words
    def who(self):
        return self.person
    def says(self):
        return self.words
class QuestionQuote(Quote):
    def says(self):
        return self.words+"?"
class ExclaimQuote(Quote):
    def says(self):
        return self.words+"!"
class BablingBrook():
    def who(self):
        return "Brook"
    def says(self):
        return "Babble"

class word():
    def __init__(self,text):
        self.text=text
    def __eq__(self,word2):
        return self.text.lower()==word2.text.lower()
    def __str__(self):
        return self.text