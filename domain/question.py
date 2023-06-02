# -*- coding: utf-8 -*-

import os


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
