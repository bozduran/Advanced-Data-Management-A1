import timeit
from operator import itemgetter

sortedTitleRatingsTsv = "sorted.title.ratings.tsv"
ratingScale = [[0.1, 1.0], [1.1, 2.0], [2.1, 3.0], [3.1, 4.0], [4.1, 5.0], [5.1, 6.0], [6.1, 7.0], [7.1, 8.0],
               [8.1, 9.0], [9.1, 10.0]]


def Q21sort():
    listOfRating = []
    #openfile
    r = open(sortedTitleRatingsTsv, "r")
    #read sortedRatitns to memory
    row = r.readline().replace("\n", "").split("\t")#skip file header
    row = r.readline().replace("\n", "").split("\t")
    while (row[0] != ""):
        row[1] = float(row[1])
        listOfRating.append(row)
        row = r.readline().replace("\n", "").split("\t")

    ratingSorted = sorted(listOfRating, key=itemgetter(1)) #sort rating in col 1(2nd....) actual rating

    sCounter = 0
    rCounter = 0

    outputList = [0] * 10 #initialized outputlist 10 items at 0 used as counter

    #count all ratings
    while (sCounter < len(ratingScale) and rCounter < len(ratingSorted)):
        if ( ratingScale[sCounter][0] <= ratingSorted[rCounter][1] <= ratingScale[sCounter][1] ):
            outputList[sCounter] = outputList[sCounter] + 1
            rCounter=rCounter+1
        elif (ratingScale[sCounter][1] < ratingSorted[rCounter][1] ):
            sCounter=sCounter+1

    #print
    for i in range(10):
        print(ratingScale[i][0]," - " ,ratingScale[i][1] , " : " ,outputList[i] )


def hashF(input):
    input = float(input)
    roundedInp = round(input)
    if (input-roundedInp == 0):
        return roundedInp
    elif(roundedInp > input ):
        return roundedInp
    else:
        return roundedInp+1

def Q21hash():
    #openfile
    hTable = {}
    r = open(sortedTitleRatingsTsv, "r")
    #read ratings
    row = r.readline().replace("\n", "").split("\t") #skip file header
    row = r.readline().replace("\n", "").split("\t")
    while (row[0] != ""):
        hashValue =hashF(row[1])
        if (hashValue not in hTable):
            hTable[hashValue]=1
        else:
            hTable[hashValue] = hTable[hashValue] + 1
        row = r.readline().replace("\n", "").split("\t")
    #print
    for i in range(10):
        print(ratingScale[i][0]," - " ,ratingScale[i][1], " : " ,hTable.get(i+1) )





startTime = timeit.default_timer()
Q21sort()
endTime = timeit.default_timer() - startTime
print("Sorting edition time ", round(endTime,2) ," sec")


startTime = timeit.default_timer()
Q21hash()
endTime = timeit.default_timer() - startTime
print("Hash edition time ", round(endTime,2) ," sec")
