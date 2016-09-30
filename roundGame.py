# coding=UTF-8

from time import time
from questionGenerator import questionGenerator
from questionSumGenerator import questionSumGenerator
from questionSubGenerator import questionSubGenerator
from printScreen import printScreen
from gameStatistics import gameStatistics
import random
import re
import math

#Class that manage every gameplay
class roundGame:

    #Constructor
    def __init__(self,type):
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

        #Type question
        self.type = type

    #Start the game
    def start(self):

        #Main objects
        if (self.type == 'mult'):
            question = questionGenerator()
        elif (self.type == 'sum'):
            question = questionSumGenerator()
        elif (self.type == 'sub'):
            question = questionSubGenerator()
        screen = printScreen()
        statistics = gameStatistics()

        #Show initial message
        screen.howToPlay()

        #Time
        initialGameTime = time()

        #If the last question was correctly answered
        isCorrect = True

        #Gameplay condition
        while self.wrong < 5 and self.round < 20:

            #Set level difficulty
            self.level = question.updateLevel(self.round)

            #Print the reader
            screen.printHeader(self.right, self.wrong, self.round, self.score)
            #Generate the question
            question.generate(self.level)
            #Print the feedback
            screen.feedBack(self.round, isCorrect)
            #Print the question
            if (self.type == 'mult'):
                screen.printQuestion(question.a, question.b)
            elif (self.type == 'sum'):
                screen.printSumQuestion(question.a, question.b)
            elif (self.type == 'sub'):
                screen.printSubQuestion(question.a, question.b)

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
                isCorrect = True
                #Score
                score = math.ceil(5-questionDuration)
                if ( score <= 1 ):
                    self.score += 1
                else:
                    self.score += score
            else:
                self.wrong += 1
                isCorrect = False
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
        statistics.saveRecords( self.round, self.right, self.wrong, self.duration, self.questionMeanDuration, self.score, self.type )

        #End game
        screen.endGame(math.floor(self.duration))


