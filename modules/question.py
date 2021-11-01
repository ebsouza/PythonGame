# -*- coding: utf-8 -*-

import random
import os
import time


class SumGenerator:

    def generate_question(self, n=10):
        question_list = list()

        while len(question_list) < n:
            a = random.randint(10, 20)
            b = random.randint(10, 20)

            alternatives = self.generate_alternatives(a, b)

            text = f"{a} + {b}"
            question = Question(alternatives=alternatives, text=text)

            if question in question_list:
                continue

            question_list.append(question)

        return question_list

    def generate_alternatives(self, a, b):
        keys = ("ans", "a", "b", "c", "d")
        alternatives = dict.fromkeys(keys, a + b)

        increment_list = list()
        do_not_increment = ["ans", random.choice(keys[1:])]

        for key, value in alternatives.items():
            if key in do_not_increment:
                continue

            increment = random.randint(-5, 5)
            while increment == 0 or increment in increment_list:
                increment = random.randint(-5, 5)
                increment_list.append(increment)

            alternatives[key] = value + increment

        return alternatives


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
        "2": SumGenerator(),
        "3": SumGenerator(),
        "4": SumGenerator()
    }

    def __init__(self, generator_code, prev_screen):
        self.generator = self.GENERATOR_MAPPER[generator_code]
        self.result = {}
        self.prev_screen = prev_screen

    def requestInput(self):
        c = input("")

        if c.lower() == "sair":
            self.prev_screen["reference"].print()
        else:
            self.execute()
            print("Parabéns você completou a partida.")
            print(self.result)
            time.sleep(5)
            self.prev_screen["reference"].print()

    def execute(self):
        questions = self.generator.generate_question(2)
        self.result = {"correct": 0, "incorrect": 0}

        for question in questions:
            question.print()
            self.check_answer(question)
            time.sleep(1)
        os.system("clear")

    def check_answer(self, question):
        print("")
        ans = int(input("Resposta: "))

        if question.alternatives["ans"] == ans:
            self.result["correct"] += 1
            print("Respota correta :)")
        else:
            self.result["incorrect"] += 1
            print("Resposta INcorreta :/")

    def print(self):
        os.system("clear")
        print("Preparado para iniciar uma nova partida? \n")
        print("- Pressione qualquer tecla para INICIAR.")
        print("- Digite SAIR para voltar a tela anterior.")
        self.requestInput()
