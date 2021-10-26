# coding=UTF-8

import random


# Class that generate questions
class questionSubGenerator:

    # Constructor
    def __init__(self):
        # Values generated in ( a - b ) form
        self.a = 0
        self.b = 0
        # Stores last numbers generated
        self.historicalA = []
        self.historicalB = []
        # Answer of the question, ans = a - b
        self.ans = 0
        # Range of numbers in each level
        self.minMaxLevels = {1: [1, 10], 2: [8, 14], 3: [16, 22], 4: [26, 33], 5: [41, 50]}

    # Generates the ( ans = a x b ) expression in 6 difficulty levels
    def generate(self, level):
        # Every new question is valid by default
        invalid = True
        # While the generated question isn't valid
        while invalid:
            # Generates Min and Max values to A and B in function of the informed level
            minA, maxA, minB, maxB = self.randomMinMax(level)
            # Generates the multiplication pair ( a x b )
            self.a = random.randint(minA, maxA)
            self.b = random.randint(minB, maxB)

            # Ensures that A and B aren't equal to 1
            while self.a == 1 and self.b == 1:
                self.a = random.randint(minA, maxA)
                self.b = random.randint(minB, maxB)

            # True if A and B is a valid pair
            invalid = self.validateQuestion(self.a, self.b)

        # Updates the historical of A and B
        self.updateHistoricalList(self.a, self.b)

        # Answer of the generated question ( ans = a x b )
        self.ans = self.a - self.b

    # Checks if A - B is a valid question
    def validateQuestion(self, a, b):

        if self.a == self.b:
            self.a += random.randint(1, 5)

        # Change a,b if a-b<0
        if (self.a - self.b) < 0:
            aux = self.b
            self.b = self.a
            self.a = aux

        # Compares the current generated numbers with respective historical
        for i in range(len(self.historicalA)):
            A = self.historicalA[i]
            B = self.historicalB[i]
            if a == A or b == B:
                return True

        return False

    # Updates the A, B historical
    def updateHistoricalList(self, a, b):
        # Add the new generated valid values
        self.historicalA.append(a)
        self.historicalB.append(b)
        # Remove the old values like a queue
        # The historical structure stores the last 1 generated numbers
        if len(self.historicalA) == 3:
            self.historicalA.pop(0)
            self.historicalB.pop(0)

    # Returns the min/max of A and B in function of informed level
    def randomMinMax(self, level):
        # Level 1
        if level == 1:
            minA, maxA = self.minMaxLevels[1]
            minB, maxB = self.minMaxLevels[1]
            return minA, maxA, minB, maxB
        # Level 2
        elif level == 2:
            minA, maxA = self.minMaxLevels[2]
            minB, maxB = self.minMaxLevels[1]
            return minA, maxA, minB, maxB
        # Level 3
        elif level == 3:
            minA, maxA = self.minMaxLevels[3]
            minB, maxB = self.minMaxLevels[2]
            return minA, maxA, minB, maxB
        # Level 4
        elif level == 4:
            minA, maxA = self.minMaxLevels[4]
            minB, maxB = self.minMaxLevels[3]
            return minA, maxA, minB, maxB
        # Level 5
        else:
            minA, maxA = self.minMaxLevels[5]
            minB, maxB = self.minMaxLevels[4]
            return minA, maxA, minB, maxB

    # Set level difficulty
    def updateLevel(self, round):
        # Define which round the level need to increase
        rlRelation = [3, 9, 16, 19, 21]

        if round < rlRelation[0]:
            return 1
        elif rlRelation[0] <= round < rlRelation[1]:
            return 2
        elif rlRelation[1] <= round < rlRelation[2]:
            return 3
        elif rlRelation[2] <= round < rlRelation[3]:
            return 4
        elif rlRelation[3] <= round < rlRelation[4]:
            return 5
        else:
            return random.randint(4, 6)
