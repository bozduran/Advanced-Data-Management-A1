sortedTitleBasicsTsv = "sorted.title.basics.tsv"
sortedTitleRatingsTsv = "sorted.title.ratings.tsv"

def Q1_3():
    #open files
    titleBasic = open(sortedTitleBasicsTsv, "r")
    titleRatings = open(sortedTitleRatingsTsv, "r")
    outputFile = open("outputQ1_3.txt", "w")
    #read line by line
    titleBasicRow = (titleBasic.readline()).replace("\n","").split("\t")
    titleRatingsRow = (titleRatings.readline()).replace("\n","").split("\t")
    #write header
    out = str(titleBasicRow[2] +"\n")
    outputFile.write(out)

    while (titleBasicRow[0] != "" and titleRatingsRow[0] != ""):
        if(titleBasicRow[0] == titleRatingsRow[0]):
            titleBasicRow = (titleBasic.readline()).replace("\n", "").split("\t")
            titleRatingsRow = (titleRatings.readline()).replace("\n", "").split("\t")
        elif (titleBasicRow[0] <  titleRatingsRow[0]):
            out = str ( titleBasicRow[2] + "\n")
            outputFile.write(out) #write output
            titleBasicRow = (titleBasic.readline()).replace("\n", "").split("\t")
        else:
            titleRatingsRow = (titleRatings.readline()).replace("\n", "").split("\t")

    #close files
    titleBasic.close()
    titleRatings.close()
    outputFile.close()
    print("Q1.3 ended:")


Q1_3()
