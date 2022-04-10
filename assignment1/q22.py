sortedTitleRatingsTsv = "sorted.title.ratings.tsv"
sortedTitleBasicsTsv = "sorted.title.basics.tsv"


def Q22():
    #open files
    r = open(sortedTitleBasicsTsv,"r")
    s = open(sortedTitleRatingsTsv,"r")
    #dictionary
    ratingCounter = {}
    rRow = r.readline().replace("\n","").split("\t") #skip colums names
    sRow = s.readline().replace("\n","").split("\t") #skip colums names

    rRow = r.readline().replace("\n","").split("\t") #read first row
    sRow = s.readline().replace("\n","").split("\t") #read first row
    #merge join
    while (rRow[0] != "" and sRow[0] != ""):
        if (rRow[0] == sRow[0]):
            if rRow[5] not in ratingCounter and "N" not in rRow[5]:
                ratingCounter[rRow[5]] = [float(sRow[1]),1]
            elif("N" not in rRow[5]):
                ratingCounter[rRow[5]][0] = ratingCounter[rRow[5]][0] + float(sRow[1])
                ratingCounter[rRow[5]][1] = ratingCounter[rRow[5]][1] + 1
            rRow = r.readline().replace("\n", "").split("\t")  # read first row
            sRow = s.readline().replace("\n", "").split("\t")  # read first row
        elif(rRow[0] < sRow[0]):
            rRow = r.readline().replace("\n","").split("\t")
        else:
            sRow = s.readline().replace("\n","").split("\t")

    #print output
    for key in sorted(ratingCounter.keys()):
        print("year: ",key," average rating: ",round(ratingCounter[key][0]/ratingCounter[key][1],2))
    #close files
    r.close()
    s.close()


Q22()
