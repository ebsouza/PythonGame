# coding=UTF-8

from time import time
from questionGenerator import questionGenerator
from printScreen import printScreen
from gameStatistics import gameStatistics
import random
import re
import math

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
        self.duration = 0
        self.questionMeanDuration = 0

	#Player score
        self.score = 0

    #Start the game
    def start(self):

        #Main objects
        question = questionGenerator()
        screen = printScreen()
        statistics = gameStatistics()

        #Show initial message
        screen.howToPlay()

        #Time
        initialGameTime = time()

        #Gameplay condition
        while self.wrong <= 5 and self.round < 20:

            #Set level difficulty
            self.level = self.updateLevel(self.round)

            #Generate the reader
            screen.printHeader(self.right, self.wrong, self.round, self.score)
            #Generate the question
            question.generate(self.level)
            #Print the question
            screen.printQuestion( question.a, question.b )

            #Question time
            initialQuestionTime = time()

            #User answer
            validInput = False
            pattern = r"^[0-9]([0-9])*$"
            while (not validInput):
                choose = raw_input()
                if re.match(pattern, choose):
                    validInput = True
                else:
                    print 'Entrada inválida'
            choose = int(choose)

            #Question duration
            questionDuration = time() - initialQuestionTime
            self.questionMeanDuration += questionDuration

            #Checking the answer
            if ( question.ans == choose ):
                self.right += 1
                #Score
                score = math.ceil(5-questionDuration)
                if ( score <= 1 ):
                    self.score += 1
                else:
                    self.score += score
            else:
                self.wrong += 1
                #Score
                if ( questionDuration < 5 ):
                    self.score += 1

            self.round += 1

            #Screen cleaning
            screen.resetScreen()

        #Gameplay duration
        self.duration = time() - initialGameTime

        #Question mean duration
        self.questionMeanDuration /= self.round

        #Save Statistics
        statistics.saveRecords( self.round, self.right, self.wrong, self.duration, self.questionMeanDuration, self.score )

    #Set level difficulty
    def updateLevel(self, round):
        #Define which round the level need to increase
        rlRelation=[2,5,8,12,16,21]

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
