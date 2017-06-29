import csv
with open("csvWrite","r") as fin:
    csvReader=csv.reader(fin)
    output=[row for row in csvReader]
print(output)

with open("csvWrite","r") as dfin:
    dictReader=csv.DictReader(dfin,fieldnames={"first","last"})
    outputDict=[row for row in dictReader]
print(outputDict)