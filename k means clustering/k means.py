def dist(src,dest):
    dist = 0
    for i in range(len(src)):
        dist+= (src[i]-dest[i])**2
    return dist**.5

def calcCentroid(cluster):
    center = []
    s = 0
    for dim in range(len(cluster[0])):
        for point in cluster:
            s+=point[dim]
        center.append(float(s)/len(cluster))
        s = 0
    return center
            

file = open('C:\\Users\\abhit\\Desktop\\data mining\\k means clustering\\training.csv')
data = []
for line in file:
    data.append([int(x) for x in line.split(',')])

k = int(input('no of clusters = '))
centroids = [x for x in data[:k]]
newClusters, newSSE = [[] for i in range(k)], 0
oldClusters, oldSSE = [[] for i in range(k)], -1

while(oldSSE != newSSE):
    oldSSE = newSSE
    for i in range(k):
        newClusters[i] = []

    newSSE = 0
    for i in range(len(data)):
        distances = [dist(data[i],centroid) for centroid in centroids]
        minIndex = distances.index(min(distances))
        newClusters[minIndex].append(data[i])
        newSSE += dist(data[i],centroids[minIndex])

    for clusterNo in range(k):
        centroids[clusterNo] = calcCentroid(newClusters[clusterNo])

    for i in range(k):
        oldClusters[i] = newClusters[i]
  
for i in range(k):
    print("centroid = "+str(centroids[i])+" cluster = "+str(oldClusters[i]))

    


