# Herda de um generator genérico
class SumGenerator():
    def __init__(self, level):
        self.pairs = []
        self.questions = []
        self.level = level

    def generate(self, n=10):
        pass

    def isValid(self, pair):
        pass


class Question():
    def __init__(self, a, b, type_):
        self.a = a
        self.b = b
        self.answer = self.getAnswer()
        self.type = type_

    def getAnswer(self):
        pass

    def print(self):
        if self.type_ == "sum":
            print(f"{self.a} + {self.b}")

