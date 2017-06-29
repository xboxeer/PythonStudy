import csv
myData=[\
{"first":"Doctor","last":"No"},\
{"first":"Rosa","last":"kleb"},\
{"first":"Mister","last":"Bug"},\
{"first":"Auric","last":"Goldfinger"}]
with open('villains','wt') as fout:
    cout=csv.DictWriter(fout,fieldnames=['first','last'])
    cout.writeheader()
    cout.writerows(myData)