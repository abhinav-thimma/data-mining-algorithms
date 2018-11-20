def euclid(tup1, tup2):
    dist = 0
    for index in range(len(tup1)):
        dist += (tup1[index] - tup2[index])**2
    return dist**0.5

def mostCommon(data, dataPoint, k):
    distances = [(euclid(dataPoint, row[:-1]), row[-1]) for row in data]
    distances.sort(key = lambda x:x[0])

    #considerin only top k shortest distances
    distances = distances[:k]
    classLabels = [dist[1] for dist in distances]
    mostCommonClass = max(set(classLabels), key = classLabels.count)
    print("k nearest neighbour classes = "+str(classLabels))
    return mostCommonClass


dataFile = open('./training.csv')
data = []
for line in dataFile:
    data.append([int(x) for x in line.split(',')])


#accepting new data point to classify
dataPoint = [int(x) for x in input("Enter values for input data point (comma seperated):").split(',')]
k = int(input("Enter a k value :"))


print("predicted class  = "+str(mostCommon(data, dataPoint, k)))

