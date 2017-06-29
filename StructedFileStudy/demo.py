import csv
data=[["Doctor","No"],["Rosa","Kleb"],["Mister","Big"]]
with open("csvWrite","wt") as fout:
    csvWriter=csv.writer(fout)
    csvWriter.writerows(data)
    
