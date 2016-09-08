# coding=UTF-8

import os

#Class that save main records and statistics
class gameStatistics():

    #Constructor
    def __init__(self):
        self.file = open("statistics.csv", "a")
        fileSize = os.path.getsize("statistics.csv")

        # if fileSize > 0:
        #     self.file.write('\n')
        #     self.file.write('\n')
        # else:
        #     self.file.write('Rounds    Right    Wrong    Duration' )
        if fileSize == 0:
            self.file.write('Rounds    Right    Wrong    Duration')


    #Saves the main records
    def saveRecords(self, rounds, right, wrong, duration):
        self.file.write( '\n' + str(rounds) + '        ' + str(right) + '        ' + str(wrong) + '       ' + str(duration) )

    #Closes file when this is destructed
    def __del__(self):
        self.file.close()