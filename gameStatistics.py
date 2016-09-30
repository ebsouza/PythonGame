# coding=UTF-8

import os

#Class that save main records and statistics
class gameStatistics():

    #Constructor
    def __init__(self):
        #Open or create statistics.csv file
        self.file = open("statistics.csv", "a")

        #Create header in new file
        fileSize = os.path.getsize("statistics.csv")
        if fileSize == 0:
            self.file.write('Rounds    Right    Wrong    Duration        qMeanDuration    Score   typeQuestion')


    #Saves the main records
    def saveRecords(self, rounds, right, wrong, duration, qMeanDuration, score, typeQuestion):
        self.file.write( '\n' + str(rounds) + '        ' + str(right) + '        ' + str(wrong) + '       ' + str(duration) +
                         '     ' + str(qMeanDuration) + '     ' + str(score) + '    ' + str(typeQuestion) )

    #Closes file when this is destructed
    def __del__(self):
        self.file.close()