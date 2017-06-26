weekdays=["monday","tuesday","wednesday","thuesday"]
fruits=["banana","orange","peach"]
drinks=["coffee","tee","beer"]
for day, fruit,drink in zip(weekdays,fruits,drinks):
    print(day, fruit,drink)

englist="Monday","Tuesday","Wednesday"
french="Lundi","Mardi","Mercredi"
dictList=list(zip(englist,french))
myDict=dict(dictList)
print(dictList) 
print(myDict)

for num in range(5):
    print(num)
for num in range(5,-1,-1):
    print(num)

#numberList=[number for number in range(1,6) if number % 2==0]
#print(numberList)
cells=[(row,col) for row in range(1,4) for col in range(1,3)]
for cell in cells:
    print(cell)
word="letters"
letterCount={letter: word.count(letter) for letter in word}
print(letterCount)