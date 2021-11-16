# -*- coding: utf-8 -*-

import random
import os
import time
from abc import ABC, abstractmethod

from modules.statistics import Statistics


class QuestionGenerator(ABC):

    operation_mapper = {
                        "+": lambda a, b: a + b,
                        "-": lambda a, b: a - b,
                        "*": lambda a, b: a * b,
                        "/": lambda a, b: a / b,
                        }

    def __init__(self, operation):
        self.operation = operation

    def text(self, a, b):
        return f"{a} {self.operation} {b}"

    def operate(self, a, b):
        operation = self.operation_mapper[self.operation]
        return operation(a, b)

    @abstractmethod
    def generate_a_b(self):
        pass

    def generate_question(self, n=10):
        question_list = list()

        while len(question_list) < n:
            a, b = self.generate_a_b()

            alternatives = self.generate_alternatives(a, b)

            text = self.text(a, b)
            question = Question(alternatives=alternatives, text=text)

            if question in question_list:
                continue

            question_list.append(question)

        return question_list

    def generate_alternatives(self, a, b):
        from modules.utils import unique_non_zero_random_numbers
        keys = ("ans", "a", "b", "c", "d")
        answer = self.operate(a, b)
        alternatives = dict.fromkeys(keys, answer)

        increment_list = unique_non_zero_random_numbers(length=3,
                                                        min_max=(-5, 5))
        increment_index = 0
        do_not_increment = ["ans", random.choice(keys[1:])]

        for key, value in alternatives.items():
            if key in do_not_increment:
                continue

            alternatives[key] = value + increment_list[increment_index]
            increment_index += 1

        return alternatives


class SumGenerator(QuestionGenerator):

    def __init__(self):
        super().__init__("+")

    def generate_a_b(self):
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        return a, b


class SubGenerator(QuestionGenerator):

    def __init__(self):
        super().__init__("-")

    def generate_a_b(self):
        a = random.randint(15, 30)
        b = random.randint(10, 20)
        if a < b:
            return b, a
        return a, b


class MultGenerator(QuestionGenerator):

    def __init__(self):
        super().__init__("*")

    def generate_a_b(self):
        a = random.randint(5, 10)
        b = random.randint(5, 10)
        if a > b:
            return b, a
        return a, b


class Question:

    def __init__(self, alternatives, text):
        self.alternatives = alternatives
        self.text = text

    def __str__(self):
        return self.text

    def __eq__(self, question):
        return self.text == question.text

    def print(self):
        os.system("clear")
        print("Questão")
        print(self.text)

        print("")
        print("Alternativas")
        print(f'a) {self.alternatives["a"]}')
        print(f'b) {self.alternatives["b"]}')
        print(f'c) {self.alternatives["c"]}')
        print(f'd) {self.alternatives["d"]}')


class Manager:

    GENERATOR_MAPPER = {
        "1": SumGenerator(),
        "2": SubGenerator(),
        "3": MultGenerator()
    }

    def __init__(self, generator_code, prev_screen):
        self.generator = self.GENERATOR_MAPPER[generator_code]
        self.result = dict()
        self.prev_screen = prev_screen
        self.statistics = Statistics()

    def requestInput(self):
        c = input("")

        if c.lower() == "sair":
            self.prev_screen["reference"].print()
        else:
            self.execute()
            self.statistics.saveRecords(self.result["correct"],
                                        self.result["incorrect"],
                                        self.result["duration"])
            time.sleep(5)
            self.prev_screen["reference"].print()

    def execute(self):
        questions = self.generator.generate_question(5)
        self.init_result()

        start_time = time.time()
        for question in questions:
            question.print()
            self.check_answer(question)
            time.sleep(1)

        self.result["duration"] = time.time() - start_time
        os.system("clear")
        self.print_result()

    def init_result(self):
        self.result = {"correct": 0,
                       "incorrect": 0,
                       "duration": 0}

    def check_answer(self, question):
        print("")
        ans = int(input("Resultado a operação: "))

        if question.alternatives["ans"] == ans:
            self.result["correct"] += 1
            print("\nResposta CORRETA")
        else:
            self.result["incorrect"] += 1
            print("\nResposta incorreta")

    def print_result(self):
        print("Parabéns! Você completou a partida. \n")
        print("Acertos: {}".format(self.result["correct"]))
        print("Erros: {}".format(self.result["incorrect"]))
        print("Duração: {:.1f} segundos".format(self.result["duration"]))

    def print(self):
        os.system("clear")
        print("Preparado para iniciar uma nova partida? \n")
        print("- Digite sempre o valor do resultado da questão.")
        print("- Pressione qualquer tecla para INICIAR.")
        print("- Digite SAIR para voltar a tela anterior.")
        self.requestInput()
