import demoClass
temp1=demoClass.myClass()
temp2=demoClass.myClass()
temp3=demoClass.myClass()
demoClass.myClass.getCount()

hunter=demoClass.Quote("Elendil","I'm hunting")
print(hunter.who()+" says "+hunter.says())
hunter1=demoClass.QuestionQuote("Elendil","I'm hunting")
print(hunter1.who()+" says "+hunter1.says())
babble=demoClass.BablingBrook()
def who_says(obj):
    print(obj.who()+" says "+obj.says())
who_says(hunter1)
who_says(babble)

word1=demoClass.word("haha")
word2=demoClass.word("HAHa")
print(word1==word2)
print(word1)