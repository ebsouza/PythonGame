# coding=UTF-8

import random

#Class that generate questions
class questionGenerator:

    #Constructor
    def __init__(self):
        #Values generated in ( a x b ) form
        self.a = 0
        self.b = 0
        #Stores last numbers generated
        self.historicalA = []
        self.historicalB = []
        #Answer of the question, ans = a x b
        self.ans = 0
        #Range of numbers(1-10) in 3 levels
        self.minMaxLevels = { 1:[1,3] , 2:[4,6] , 3:[7,9] }

    #Generates the ( ans = a x b ) expression in 6 difficulty levels
    def generate(self, level):
        #Every new question is valid by default
        invalid = True
        #While the generated question isn't valid
        while invalid:
            #Generates Min and Max values to A and B in function of the informed level
            minA, maxA, minB, maxB = self.randomMinMax(level)
            #Generates the multiplication pair ( a x b )
            self.a = random.randint(minA,maxA)
            self.b = random.randint(minB,maxB)

            #Ensures that A and B aren't equal to 1
            while self.a == 1 and self.b==1:
                self.a = random.randint(minA,maxA)
                self.b = random.randint(minB,maxB)

            #True if A and B is a valid pair
            invalid = self.validateQuestion(self.a,self.b)


        #Updates the historical of A and B
        self.updateHistoricalList( self.a, self.b )

        #Answer of the generated question ( ans = a x b )
        self.ans = self.a * self.b

    #Checks if A x B is a valid question
    # ( This need to be tested )!!!
    def validateQuestion(self,a,b):
        #Compares the current generated numbers with respective historical
        for i in range(len(self.historicalA)):
            if ( a == self.historicalA[i] or b == self.historicalB[i] ):
                return True
        return False

    #Updates the A, B historical
    #( This need to be tested )!!!
    def updateHistoricalList(self,a,b):
        #Add the new generated valid values
        self.historicalA.append(a)
        self.historicalB.append(b)
        #Remove the old values like a queue
        #The historical structure stores the last 1 generated numbers
        if ( len(self.historicalA) == 2 ):
            self.historicalA.pop(0)
            self.historicalB.pop(0)

    #Returns the min/max of A and B in function of informed level
    def randomMinMax(self,level):
        #Level 1 - A:(1,3) ; B(1:3)
        if level == 1:
            minA, maxA = self.minMaxLevels[1]
            minB, maxB = self.minMaxLevels[1]
            return minA, maxA, minB, maxB
        # Level 2 - A:(1,3) ; B(4:6)
        elif level == 2:
            minA, maxA = self.minMaxLevels[1]
            minB, maxB = self.minMaxLevels[2]
            return minA, maxA, minB, maxB
        # Level 3 - A:(1,3) ; B(7:9)
        elif level == 3:
            minA, maxA = self.minMaxLevels[1]
            minB, maxB = self.minMaxLevels[3]
            return minA, maxA, minB, maxB
        # Level 4 - A:(4,6) ; B(4:6)
        elif level == 4:
            minA, maxA = self.minMaxLevels[2]
            minB, maxB = self.minMaxLevels[2]
            return minA, maxA, minB, maxB
        # Level 5 - A:(4,6) ; B(7:9)
        elif level == 5:
            minA, maxA = self.minMaxLevels[2]
            minB, maxB = self.minMaxLevels[3]
            return minA, maxA, minB, maxB
        # Level 6 - A:(7,9) ; B(7:9)
        else:
            minA, maxA = self.minMaxLevels[3]
            minB, maxB = self.minMaxLevels[3]
            return minA, maxA, minB, maxB