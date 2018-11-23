dataFile = open('./training_binary.csv')
data = []
for line in dataFile:
    data.append([int(x) for x in line.split(',')])

def getConfusionMat(tup1, tup2):
    count11, count10, count01, count00 = 0,0,0,0
    for index in range(len(tup1)):
        if(tup1[index] == 0 and tup2[index] == 0):
            count00+=1
        elif(tup1[index] == 0 and tup2[index] == 1):
            count01+=1
        elif(tup1[index] == 1 and tup2[index] == 0):
            count10+=1
        elif(tup1[index] == 1 and tup2[index] == 1):
            count11+=1

    return (count11, count10, count01, count00)

def jaccard(tup1, tup2):
    q,r,s,t = getConfusionMat(tup1, tup2)
    if(q+r+s == 0):
        return "NaN"
    return float(q)/(q+r+s)

def dissim_asymmetric(tup1, tup2):
    q,r,s,t = getConfusionMat(tup1, tup2)
    if(q+r+s+t == 0):
        return "NaN"
    return float(r+s)/(q+r+s)

def dissim_symmetric(tup1, tup2):
    q,r,s,t = getConfusionMat(tup1, tup2)
    if(q+r+s+t == 0):
        return "NaN"
    return float(r+s)/(q+r+s+t)

#function to print proximity matrix
def printProxMatrix(data, function):
    for i in range(len(data)):
        for j in range(len(data)):
            print(str(function(data[i],data[j])), end = ' ')
        print("")
    print("\n\n\n")

printProxMatrix(data, jaccard)
printProxMatrix(data, dissim_asymmetric)
printProxMatrix(data, dissim_symmetric)
