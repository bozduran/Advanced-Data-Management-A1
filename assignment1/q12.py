sortedTitleBasicsTsv = "sorted.title.basics.tsv"
sortedTitleEpisodeTsv = "sorted.title.episode.tsv"

def Q1_2():
    #open files
    titleBasic = open(sortedTitleBasicsTsv, "r")
    titleEpisode = open(sortedTitleEpisodeTsv, "r")
    outputFile = open("outputQ1_2.txt", "w")
    #read line by line
    titleBasicRow = (titleBasic.readline()).replace("\n","").split("\t")
    titleEpisodeRow = (titleEpisode.readline()).replace("\n","").split("\t")
    out = str(titleBasicRow[2] + " " + titleEpisodeRow[1] + " " + titleEpisodeRow[2] + "\n")
    outputFile.write(out) # file header

    while(titleBasicRow[0] != "" and titleEpisodeRow[0] != ""):
        if( titleBasicRow[0] == titleEpisodeRow[0] ):
            if(titleEpisodeRow[3] == "1"):
                out = str(titleBasicRow[2]+" "+titleEpisodeRow[1]+" "+titleEpisodeRow[2]+"\n")
                outputFile.write(out) #write putput
            titleBasicRow = (titleBasic.readline()).replace("\n", "").split("\t")
            titleEpisodeRow = (titleEpisode.readline()).replace("\n", "").split("\t")
        elif(titleBasicRow[0] < titleEpisodeRow[0]):
            titleBasicRow = (titleBasic.readline()).replace("\n", "").split("\t")
        else:
            titleEpisodeRow = (titleEpisode.readline()).replace("\n", "").split("\t")
    #close files
    titleBasic.close()
    titleEpisode.close()
    outputFile.close()
    print("Q1.2 ended:")

Q1_2()
