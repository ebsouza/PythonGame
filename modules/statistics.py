# coding=UTF-8

import os

class Statistics:

    def __init__(self):
        self.file = open("statistics.csv", "a")

        if os.path.getsize("statistics.csv") == 0:
            self.create_header()

        self.file.close()

    def create_header(self):
        self.file.write('Correct, Incorrect, Duration(s)')

    def saveRecords(self, correct, incorrect, duration):
        self.file = open("statistics.csv", "a")
        self.file.write('\n' + str(correct) + ', ' + str(incorrect) + ',  ' + str(duration))
        self.file.close()
