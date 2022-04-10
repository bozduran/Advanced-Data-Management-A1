
sortedTitleBasicsTsv = "sorted.title.basics.tsv"
sortedTitleCrewTsv = "sorted.title.crew.tsv"

def Q1_1():
    #open files
    titleBasic = open(sortedTitleBasicsTsv,"r")
    titleCrew = open(sortedTitleCrewTsv,"r")
    outputFile = open("outputQ1_1.txt", "w")

    #read line by line
    titleBasicRow = (titleBasic.readline()).replace("\n","").split("\t")
    titleCrewRow  = (titleCrew.readline()).replace("\n","").split("\t")

    outputFile.write("primaryTitle\tdirectors\n")

    while (titleBasicRow[0] != "" and titleCrewRow[0] != ""):
        if (titleBasicRow [0] == titleCrewRow[0]):
            if( "," in titleCrewRow[1] ):
                out = str(titleBasicRow[2]+"\t"+titleCrewRow[1] + "\n")
                outputFile.write( out ) #write output line by line
            titleBasicRow = (titleBasic.readline()).replace("\n", "").split("\t")
            titleCrewRow = (titleCrew.readline()).replace("\n", "").split("\t")
        elif(titleBasicRow[0] < titleCrew[0]):
            titleBasicRow = (titleBasic.readline()).replace("\n", "").split("\t")
        else:
            titleCrewRow = (titleCrew.readline()).replace("\n", "").split("\t")
    #close files
    outputFile.close()
    titleBasic.close()
    titleCrew.close()
    print("Q1.1 ended:")

Q1_1()
