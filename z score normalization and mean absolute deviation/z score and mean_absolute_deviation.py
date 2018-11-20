def mean(arr):
    return sum(arr)/len(arr)

def mode(arr):
    return max(set(arr), key=arr.count)

def standardDeviation(arr):
    meanVal = mean(arr)
    variance = 0
    for num in arr:
        variance += ((num - meanVal)**2)
    return (variance/len(arr))**.5

def meanAbsDeviation(arr):
    meanVal = mean(arr)
    MAD = mean([abs(num - meanVal) for num in arr])
    return MAD

def zScoreCalc(arr):
    meanVal = mean(arr)
    sdVal = standardDeviation(arr)
    zScoreArr = [(num - meanVal)/sdVal for num in arr]

    return zScoreArr

def decimalScaling(arr):
    maxEleLen = 10**-len(str(max(arr)))
    return [(num*maxEleLen) for num in arr]

data = [int(num) for num  in input()]
print("mean = "+str(mean(data))+ " sd = "+str(standardDeviation(data)))
print("MAD = "+str(meanAbsDeviation(data)))
