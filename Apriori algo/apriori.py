from itertools import combinations

dataFile = open('.\data.csv')
data = []
cols = []
flip = 0
for line in dataFile:
    if(flip == 0):
        cols.extend([x.strip() for x in line.split(',')])
        flip = 1
    else:
        data.append([int(x) for x in line.split(',')])

colIndices = [i for i in range(len(cols))]

def apriori(data, min_support, level):
    comb = combinations(colIndices, level)
    rules = []
    
    
    for combination in comb:
        support = 0
        for row in data:
            flip = 1
            for index in combination:
                if(row[index] == 0):
                    flip = 0
            if(flip == 1):
                support +=1
        if(support > min_support):
            rules.append(([cols[i] for i in combination], support))

    return rules

rules = ['']
level = 1
min_support = int(input('enter min support:'))
while(rules != []):
    rules = apriori(data, min_support, level)
    print(rules)
    level+=1
