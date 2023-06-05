# -*- coding: utf-8 -*-

import random
from abc import ABC, abstractmethod

from domain.question import Question
from domain.utils import unique_non_zero_random_numbers


class QuestionGenerator(ABC):

    operation_mapper = {
                        "+": lambda a, b: a + b,
                        "-": lambda a, b: a - b,
                        "*": lambda a, b: a * b,
                        "/": lambda a, b: a / b,
                        }

    def __init__(self, operation):
        self.operation = operation

    def create_text(self, a, b):
        return f"{a} {self.operation} {b}"

    def operate(self, a, b):
        operation = self.operation_mapper[self.operation]
        return operation(a, b)

    @abstractmethod
    def generate_a_b(self):
        pass

    def generate_question(self, n=10):
        questions = list()

        while len(questions) < n:
            a, b = self.generate_a_b()

            alternatives = self.generate_alternatives(a, b)
            text = self.create_text(a, b)
            question = Question(alternatives=alternatives, text=text)

            if question in questions:
                continue

            questions.append(question)

        return questions

    def generate_alternatives(self, a, b):
        keys = ("ans", "a", "b", "c", "d")
        answer = self.operate(a, b)
        alternatives = dict.fromkeys(keys, answer)

        increment_list = unique_non_zero_random_numbers(3)
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
