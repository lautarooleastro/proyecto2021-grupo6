import csv

def getZones(nombre):
    with open(nombre, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))   
    
    with open(nombre, newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)