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

    def check_answer(self, result):
        print("")
        ans = int(input("Resposta: "))

        if self.alternatives["ans"] == ans:
            result["correct"] += 1
            print("Acertou!")
        else:
            result["incorrect"] += 1
            print("Errou!")


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
            time.sleep(5)
            self.prev_screen["reference"].print()
        elif c in ["NAO", "N"]:
            self.prev_screen["reference"].print()

    def execute(self):
        questions = self.generator.generate_question(2)
        result = {"correct": 0, "incorrect": 0}

        for question in questions:
            question.print()
            question.check_answer(result)
            time.sleep(1)
        os.system("clear")
        return result

    def print(self):
        os.system("clear")
        print("Você irá iniciar a partida escolhida.")
        print("Avançar [S]SIM / [N]NAO?")
        self.requestInput()
