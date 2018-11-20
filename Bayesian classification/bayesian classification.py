
def countYesNo(data):
    yesCount,noCount = 0, 0
    for row in data:
        if(row[4] == 1):
            yesCount+=1
        else:
            noCount+=1
    return (yesCount,noCount)

def countCorrelated(colNum, colVal, yesOrNo):
    count = 0
    for row in data:
        if(row[colNum] == colVal and row[4] == yesOrNo):
            count+=1
    return count

trainingData = open('C:\\Users\\abhit\\Desktop\\data mining\\bayesian classification\\train.csv')
data = []
for line in trainingData:
    data.append([int(x) for x in line.split(',')])

totalYes,totalNo = countYesNo(data)

if(totalYes == 0):
    print("category = No")
    exit()
elif(totalNo == 0):
    print("category = Yes")
    exit()


    
newData  = input('enter comma seperated integers for every column:')
yesScore, noScore = 1, 1

for colNum in range(len(newData)):
    yesScore *= float(countCorrelated(colNum,newData[colNum],1))/totalYes
    noScore *= float(countCorrelated(colNum,newData[colNum],2))/totalNo


print("yes score = "+str(yesScore)+"  no score = "+str(noScore))
print("category: "+("yes" if yesScore > noScore else "No"))
