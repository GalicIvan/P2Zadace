from csv import reader

with open('rezultati.csv', 'r', encoding = 'utf8') as file:
    csv_reader = reader(file)
    studenti = list(map(tuple, csv_reader))
    print(studenti)
    for student in studenti:
        if int(student[2]) > 49:
            print(student)

sortiraniStudenti = sorted(studenti, key=lambda x: x[1])
print(sortiraniStudenti)

studentiDict = {}
for st in studenti:
    if int(st[2]) < 49:
        studentiDict[1] = studentiDict.get(1, []) + [st]
    if int(st[2]) >= 50 and int(st[2]) < 65:
        studentiDict[2] = studentiDict.get(2, []) + [st]
    if int(st[2]) >= 65 and int(st[2]) < 80:
        studentiDict[3] = studentiDict.get(3, []) + [st]
    if int(st[2]) >= 80 and int(st[2]) < 90:
        studentiDict[4] = studentiDict.get(4, []) + [st]
    if int(st[2]) >= 90:
        studentiDict[5] = studentiDict.get(5, []) + [st]

for key, value in studentiDict.items():
    for item in value:
        print(key, item)