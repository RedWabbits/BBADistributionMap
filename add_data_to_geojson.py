import json
import csv


with open("./data/FinalData.csv",'r') as csvfile:
    data_reader = csv.reader(csvfile)
    index = 0
    counties = None

    file =  open('./geojson/congressional_districts_mi.json', 'r') 
    counties = json.load(file)
    file.close()

    newfile = open('./geojson/final.json', 'w')

    column_names = []
    for row in data_reader:
            if index > 0:
                for i in range(len(row)):
                    if i > 0:
                        label = column_names[i]
                        label =  label.replace(' ','')
                        label = label.replace("U.S.","US")
                        label = label.replace("U.S","US")
                        label = label.upper()
                        
                        value =  row[i].replace(',','')
                        value =  value.replace('%','')
                        value =  value.replace("N/A","0")
                        counties["features"][int(row[0])-1]["properties"][label] = float(value)
            else:
                column_names = row
            index = index + 1  

    json.dump(counties,newfile)
    newfile.close()  

