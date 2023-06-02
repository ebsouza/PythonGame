# -*- coding: utf-8 -*-

import os
import time

from domain.generator import SumGenerator, SubGenerator, MultGenerator
from domain.statistics import Statistics

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
