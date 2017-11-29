import csv
import math
import operator

def loadDataset( TrainDataFile, TestDataFile,  trainingSet=[], testSet=[]):
    with open(TrainDataFile, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(8):
                dataset[x][y] = float(dataset[x][y])
            trainingSet.append(dataset[x])

    print "Train Data File length = " , len(dataset)
    print trainingSet

    print "\n"

    with open(TestDataFile, 'r') as csvfile:
        Datalines = csv.reader(csvfile)
        dataset = list(Datalines)
        for x in range(len(dataset) - 1):
            for y in range(8):
                dataset[x][y] = float(dataset[x][y])
            testSet.append(dataset[x])

    print "Test Data File Length = " , len(dataset)
    print testSet

def euclideanDistance (x1, x2, length):
    distance = 0
    for x in range(length):
       # print "Tow Attributs" , x1 , " " , x2
        distance += pow((x1[x] - x2[x]), 2)
       # distance += (x1[x] - x2[x] ) * (x1[x] - x2[x])
       # print distance
    return math.sqrt(distance)


def get_K_Neighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))

    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def getMostFrequently(neighbors):

    MostFrequent = {}
  #  print neighbors [0]
    for x in range(len(neighbors)):
        current = neighbors[x][-1]
        #print "Current = " , current
        if current in MostFrequent:
            MostFrequent[current] += 1
        else:
            MostFrequent[current] = 1

    sortedItems = sorted(MostFrequent.items(), key=operator.itemgetter(1), reverse=True)
    return sortedItems[0][0]


def getAccuracy(testSet, predictions):
    correct = 0

    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1

    print "\nNumber of Correct = " , correct , ", Number of instances test" ,  len(testSet)
    return (correct / float(len(testSet))) * 100.0


def main():
    trainingSet = []
    testSet = []
    loadDataset('TrainData.data', 'TestData.data', trainingSet, testSet)

    predictions = []
    k = 3

    # K =  4  : 9 ->  54.27
   # print testSet[0]
   # print trainingSet

    for x in range(len(testSet)):
        neighbors = get_K_Neighbors(trainingSet, testSet[x], k)
        result = getMostFrequently(neighbors)
        predictions.append(result)
        print(' predicted=' + repr(result) + ' , actual= ' + repr(testSet[x][-1]))


    accuracy = getAccuracy(testSet, predictions)
    print "K Used  = " , k
    print('Accuracy: ' + repr(accuracy) + ' %')


if __name__ == '__main__':
    main()