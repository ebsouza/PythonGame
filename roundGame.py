# coding=UTF-8

from time import time
from questionGenerator import questionGenerator
from printScreen import printScreen
from gameStatistics import gameStatistics
import random
import re

#Class that manage every gameplay
class roundGame:

    #Constructor
    def __init__(self):
        #Right and wrong questions
        self.right = 0
        self.wrong = 0

        #Current round
        self.round = 1

        #Level difficulty
        self.level = 1

        #Time variables
        self._time = time()
        self.duration = 0

        #Objects relative Questions and Screen
        self.question = questionGenerator()
        self.screen = printScreen()

    #Start the match
    def start(self):

        statistics = gameStatistics()

        #Gameplay condition, user can miss less than four times
        while self.wrong < 10 and self.round <= 50:

            #Set level difficulty
            self.level = self.updateLevel(self.round)

            #Generate the reader
            self.screen.printHeader(self.right, self.wrong, self.round)
            #Generate the question
            self.question.generate(self.level)
            #Print the question
            self.screen.printQuestion( self.question.a, self.question.b )

            #User answer
            #choose = int(raw_input())

            validInput = False
            pattern = r"^[0-9]([0-9])*$"
            while (not validInput):
                choose = raw_input()
                if re.match(pattern, choose):
                    validInput = True
                else:
                    print 'Entrada inválida'
            choose = int(choose)

            #Checking the answer
            if ( self.question.ans == choose ):
                #One more correct answer
                self.right += 1
            else:
                #one more incorrect answer
                self.wrong += 1
            self.round += 1

            #Screen cleaning
            self.screen.resetScreen()

        #Gameplay duration
        self.duration = time() - self._time

        #Save Statistics
        statistics.saveRecords( self.round, self.right, self.wrong, self.duration )

    #Set level difficulty
    def updateLevel(self, round):
        #Define which round the level need to increase
        rlRelation=[8,16,24,32,40,48]

        if ( round < rlRelation[0]):
            return 1
        elif (rlRelation[0] <= round < rlRelation[1]):
            return 2
        elif ( rlRelation[1] <= round < rlRelation[2] ):
            return 3
        elif ( rlRelation[2] <= round < rlRelation[3] ):
            return 4
        elif ( rlRelation[3] <= round < rlRelation[4] ):
            return 5
        elif ( rlRelation[4] <= round < rlRelation[5] ):
            return 6
        else:
            return random.randint(4,6)
