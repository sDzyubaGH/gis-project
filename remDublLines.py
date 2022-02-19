import csv

idPoints = []
print('Downloading data...')
with open('IdPoints.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        point = [float(i) for i in row[0].split(';')]
        idPoints.append(point)


units = []
with open('Units.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        unit = row[0].split(';')
        units.append(unit)

print('Data downloaded\n')

f = False
duplicates = []
# counter = 0

print('Data processing...')

for i in range(len(units)):
    for j in range(i + 1, len(units)):
        if(units[j][0] == units[i][1] and units[i][4] == units[j][4]):
            for a in range(len(idPoints)):
                if(idPoints[a][0] == float(units[j][2])):
                    f = True
                    duplicates.append(idPoints[a])
                else:
                    if f: 
                        break
        if f:
            # counter = counter + 1 
            break
    f = False
                    

for el in duplicates:
    idx = idPoints.index(el)
    idPoints.pop(idx)

print('Data processed')