# Herda de um generator genérico
class SumGenerator():

    @classmethod
    def generate(cls, n=10):
        question_list = list()
        for i in range(n):
            question = Question()
            question.alternatives = [1, 2, 3, 4, 5]
            question.answer = 1
            question.question = "| Question |"
            question_list.append(question)
        return question_list


class Question():

    def __init__(self):
        self.alternatives = list()
        self.answer = None
        self.question = None

    def setAnswer(self, alternative):
        self.answer = alternative

    def setQuestion(self, question):
        self.question = question

    def __str__(self):
        return self.question


QUESTION_MAPPER = {
    "1": SumGenerator(),
    "2": SumGenerator(),
    "3": SumGenerator(),
    "4": SumGenerator()
}
