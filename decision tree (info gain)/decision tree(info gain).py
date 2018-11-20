import math

dataFile = open('./data.csv')
data = []
cols = []
flip = 0
for line in dataFile:
    if(flip == 0):
        cols.extend([x for x in line.split(',')])
        flip+=1
    else:
        data.append([int(x) for x in line.split(',')])

def calcLog(noOfMatches, totalEntries):
    if(noOfMatches == 0 or totalEntries == 0):
        noOfMatches+=1
        totalEntries+=1
    return ((float(noOfMatches)/totalEntries) * math.log(abs(float(noOfMatches)/totalEntries))/math.log(2))

def totalGain(data):
    totalYes, totalNo = [row[-1] for row in data].count(1), [row[-1] for row in data].count(0)
    total = len(data)
    return -(calcLog(totalYes,total) + calcLog(totalNo, total))

def countClassLabelMatch(data, colIndex, classNum, label):
    count = 0
    for row in data:
        if(row[colIndex] == classNum and row[-1] == label):
            count+=1
    return count

def totalGainCol(data, colName):
    colIndex = cols.index(colName)
    col = [row[colIndex] for row in data]
    classes = set(col)

    classGain = 0
    for aClass in list(classes):
        yesCount = countClassLabelMatch(data, colIndex, aClass, 1)
        noCount = countClassLabelMatch(data, colIndex, aClass, 0)
        total = yesCount + noCount

        classGain += (-1*(total/len(data))*(calcLog(yesCount,total) + calcLog(noCount, total)))

    return totalGain(data) - classGain

gains = [(totalGainCol(data, cols[i]),cols[i]) for i in range(len(cols)-1)]
gains.sort()
print(gains[::-1])
