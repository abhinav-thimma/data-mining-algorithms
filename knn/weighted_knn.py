from collections import Counter

def euclid(tup1, tup2):
    dist = 0
    for index in range(len(tup1)):
        dist += (tup1[index] - tup2[index])**2
    return dist**0.5

def mostWeightedCommon(data, dataPoint, k):
    distances = [(euclid(dataPoint, row[:-1]), row[-1]) for row in data]
    distances.sort(key = lambda x:x[0])

    #considerin only top k shortest distances
    distances = distances[:k]
    classLabels = [dist[1] for dist in distances]

    #finding no of unique class labels
    classes = set(classLabels)

    classWeights = dict()
    for aClass in classes:
        classWeights[aClass] = 0

    #computing class weights
    for ele in distances:
        classWeights[ele[1]] += 1/float(ele[0])

    mostCommonClass = max(classWeights, key = classWeights.get)
    print("class weights = "+str(classWeights))
    return mostCommonClass


dataFile = open('./training.csv')
data = []
for line in dataFile:
    data.append([int(x) for x in line.split(',')])


#accepting new data point to classify
dataPoint = [int(x) for x in input("Enter values for input data point (comma seperated):").split(',')]
k = int(input("Enter a k value :"))


print("predicted class  = "+str(mostWeightedCommon(data, dataPoint, k)))

