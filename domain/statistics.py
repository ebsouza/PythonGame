# -*- coding: utf-8 -*-

import os

from config import statistic_file


class Statistics:

    def __init__(self):
        self.file = open(statistic_file, "a")

        if os.path.getsize(statistic_file) == 0:
            self.file.write('Correct, Incorrect, Duration(s)')

        self.file.close()

    def saveRecords(self, correct, incorrect, duration):
        with open(statistic_file, "a") as file:
            file.write('\n' + str(correct) + ', ' + str(incorrect) + ',  ' + str(duration))
