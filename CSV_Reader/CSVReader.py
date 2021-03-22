import csv

def readCSV(filepath):
    rows = []
    csvFile = open(filepath)
    csvReader = csv.DictReader(csvFile, delimiter=',')
    for row in csvReader:
        rows.append(row)
    csvFile.close()
    return rows