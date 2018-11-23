

def printBoxPlot(minEle, q1, median, q3, maxEle):
    print('-----   '+str(maxEle))
    print('  |  \n  |  ')
    print('-----   '+str(q3))
    print('|   |')
    print('-----   '+str(median))
    print('|   |')
    print('-----   '+str(q1))
    print('  |  \n  |  ')
    print('-----   '+str(minEle))

    
data = [int(x) for x in input().split(',')]
minEle = min(data)
q1 = data[int(len(data)/4)]
median = data[int(len(data)/2)] if(len(data)%2 != 0) else (data[int((len(data)+1)/2)]+data[int((len(data)-1)/2)])/2
q3 = data[int(len(data)*3/4)]
maxEle = max(data)

printBoxPlot(minEle, q1, median, q3, maxEle)


    
    
