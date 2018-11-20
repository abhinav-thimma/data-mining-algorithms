dataFile = open('./training_nominal.csv')
data = []
for line in dataFile:
    data.append([int(x) for x in line.split(',')])

def matching(tup1, tup2):
    matchCount = 0
    for index in range(len(tup1)):
        if(tup1[index] == tup2[index]):
            matchCount +=1
    return (len(tup1) - matchCount)/len(tup1)

#function to print proximity matrix
def printProxMatrix(data, function):
    for i in range(len(data)):
        for j in range(len(data)):
            print(str(function(data[i],data[j])), end = ' ')
        print("")


printProxMatrix(data, matching)
