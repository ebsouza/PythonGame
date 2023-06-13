# -*- coding: utf-8 -*-

import os
import time

from domain.generator import MultGenerator, SubGenerator, SumGenerator
from domain.session import Session
from data.persist import save_session


class PlayScreen:

    GENERATOR_MAPPER = {
        "1": SumGenerator(),
        "2": SubGenerator(),
        "3": MultGenerator()
    }

    def __init__(self, generator_code, prev_screen):
        self.generator = self.GENERATOR_MAPPER[generator_code]
        self.prev_screen = prev_screen
        self.session = Session()
        self.result = {"correct": 0, "incorrect": 0}

    def request_input(self):
        c = input("")

        if c.lower() == "sair":
            self.prev_screen["reference"].print()
        else:
            self.execute()
            time.sleep(5)
            self.prev_screen["reference"].print()

    def execute(self):
        questions = self.generator.generate_question(5)

        self.session.start()
        for question in questions:
            self.print_question(question)
            self.read_answer(question)
            time.sleep(1)

        self.session.save_record(self.result)
        self.session.finish()

        print(self.result)
        print(self.session.data)

        save_session(self.session)
        os.system("clear")
        self.print_result()

    def read_answer(self, question):
        print("")
        ans = int(input("Resultado da operação: "))

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
        print("Duração: {:.1f} segundos".format(self.session.elapsed_time))

    def print(self):
        os.system("clear")
        print("Preparado para iniciar uma nova partida? \n")
        print("- Digite sempre o valor do resultado da questão.")
        print("- Pressione qualquer tecla para INICIAR.")
        print("- Digite SAIR para voltar a tela anterior.")
        self.request_input()

    def print_question(self, question):
        os.system("clear")
        print("Questão")
        print(question.text)

        print("")
        print("Alternativas")
        print(f'a) {question.alternatives["a"]}')
        print(f'b) {question.alternatives["b"]}')
        print(f'c) {question.alternatives["c"]}')
        print(f'd) {question.alternatives["d"]}')


class ExitScreen:

    def print(self):
        os.system("clear")
        print("Obrigado pela sua participação \n \n")
        print("Pressione qualquer tecla para sair")
        input("")
        time.sleep(0.5)
        os.system("clear")
        quit()
