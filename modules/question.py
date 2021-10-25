# Herda de um generator genérico
import random
import os
import time

class SumGenerator:

    def generate(self, n=10):
        question_list = list()
        for i in range(n):
            a = random.randint(10, 20)
            b = random.randint(10, 20)

            alternatives = dict()
            alternatives["ans"] = a + b
            alternatives["a"] = a + b + random.randint(-5, 5)
            alternatives["b"] = a + b + random.randint(-5, 5)
            alternatives["c"] = a + b + random.randint(-5, 5)
            alternatives["d"] = a + b + random.randint(-5, 5)

            text = f"{a} + {b}"
            question = Question(alternatives=alternatives, text=text)

            question_list.append(question)

        return question_list


class Question:

    def __init__(self, alternatives, text):
        self.alternatives = alternatives
        self.text = text

    def __str__(self):
        return self.text


QUESTION_MAPPER = {
    "1": SumGenerator(),
    "2": SumGenerator(),
    "3": SumGenerator(),
    "4": SumGenerator()
}

class Manager:

    GENERATOR_MAPPER = {
        "1": SumGenerator(),
        "2": SumGenerator(),
        "3": SumGenerator(),
        "4": SumGenerator()
    }

    def __init__(self, generator_code, prev_screen):
        self.generator = self.GENERATOR_MAPPER[generator_code]
        self.prev_screen = prev_screen

    def requestInput(self):
        c = input("")

        if c in ["SIM", "S"]:
            result = self.execute()
            print("Parabéns você completou a sua jogada.")
            print(result)
            time.sleep(2)
            self.prev_screen["reference"].print()
        elif c in ["NAO", "N"]:
            self.prev_screen["reference"].print()

    def execute(self):
        questions = self.generator.generate(5)
        result = {"correct": 0, "incorrect": 0}

        for question in questions:
            os.system("clear")
            print("Questão")
            print(question.text)

            print("")
            print("Alternativas")
            print(f'a) {question.alternatives["a"]}')
            print(f'b) {question.alternatives["b"]}')
            print(f'c) {question.alternatives["c"]}')
            print(f'd) {question.alternatives["d"]}')

            print("")
            ans = int(input("Resposta:"))

            if question.alternatives["ans"] == ans:
                result["correct"] += 1
                print("Acertou!")
            else:
                result["incorrect"] += 1
                print("Errou!")
            time.sleep(1)
        os.system("clear")
        return result

    def print(self):
        os.system("clear")
        print("Instruções aqui.")
        print("Avançar [S]SIM / [N]NAO?")
        self.requestInput()
