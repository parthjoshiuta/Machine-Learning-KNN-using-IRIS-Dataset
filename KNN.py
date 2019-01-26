import csv
import random
import math
import operator

def loadData(fn, split, trainingSet= [], testSet = []):
    with open(fn, 'r') as csvFile:
        lines = csv.reader(csvFile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else :
                testSet.append(dataset[x])

def euclideanDistance(instance1, instance2, length):
    distance = 0

    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])),2)
    return math.sqrt(distance)

def getNeighbours(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance,trainingSet[x], length)
        distances.append((trainingSet[x],dist))
    distances.sort(key = operator.itemgetter(1))
    neightbours = []
    for x in range(k):
        neightbours.append(distances[x][0])
    return neightbours

def getResponse(neighbours):
    classVotes = {}
    for x in range(len(neighbours)):
        response = neighbours[x][-1]
        if response in classVotes:
            classVotes[response]+= 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def regression(neighbours, k):
    sum = 0
    average = 0
    result = []
    for i in range(len(neighbours)):
        sum=0
        average = 0
        for j in range(k):
            sum += neighbours[j][i]
        average = sum / k
        result.append(average)
    return result

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/ float(len(testSet))) * 100.0

def main():
    # Prepare Data
    trainingSet = []
    testSet = []
    split = 0.67
    loadData('/Users/parth/PycharmProjects/MachineLearningHW1/iris.data.csv', split, trainingSet, testSet)
    print ('Train Set :' + repr(len(trainingSet)))
    print ('Test Set:' + repr(len(testSet)))
    # generate Predictions
    predictions = []
    k = 4
    print ("Do you want to do 1. regression or 2. classification ?")
    getuser = input()
    if getuser == '2' :

    # For Classification
        for x in range(len(testSet)):
            neighbours = getNeighbours(trainingSet, testSet[x], k)
            result = getResponse(neighbours)
            predictions.append(result)
            print ('> Predicted : ' + repr(result) + ', actual : ' + repr(testSet[x][-1]))
        accuracy = getAccuracy(testSet, predictions)
        print ('Accuracy: ' + repr(accuracy) + '%')
    if getuser == '1' :
    # For Regression
        for x in range(len(testSet)):
           neighbours = getNeighbours(trainingSet, testSet[x], k)
           result = regression(neighbours, k)
           predictions.append(result)
        print(predictions)
main()