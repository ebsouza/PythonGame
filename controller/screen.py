# -*- coding: utf-8 -*-

import os
import time
from abc import ABC, abstractmethod

from controller.routes import Routes
from domain.generator import MultGenerator, SubGenerator, SumGenerator
from domain.statistics import Statistics


class Screen(ABC):

    def __init__(self):
        self.routes = Routes()
        self.show_options = True

    def request_input(self):
        c = "--"
        while c not in self.routes.options:
            c = input("")
        self.next(c)

    def next(self, c):
        try:
            next_screen = self.routes.getReference(c)
            next_screen.print()
        except Exception as e:
            print(f"Desculpe, ocorreu um erro. {e}")

    def print(self):
        os.system("clear")
        self.text_screen()

        if self.show_options:
            for data in self.routes.data:
                print(f"[{data['option']}] - {data['code']} ")

        self.request_input()

    @abstractmethod
    def text_screen(self):
        pass


class MainScreen(Screen):

    def __init__(self):
        self.id = {"code": "Tela Principal",
                   "reference": self}
        super().__init__()
        self.routes.addRoute("Jogar", "1", StartToPlayScreen(self.id))
        self.routes.addRoute("Creditos", "2", CreditsScreen(self.id))
        self.routes.addRoute("Sair", "3", ExitScreen())

    def text_screen(self):
        os.system("clear")
        print("Seja bem-vindo")
        print("Escolha as opções:")


class CreditsScreen(Screen):

    def __init__(self, prev_reference):
        self.id = {"code": "credits",
                   "reference": self}
        super().__init__()
        self.routes.addRoute(prev_reference["code"], "1", prev_reference["reference"])
        self.show_options = False

    def request_input(self):
        input("")
        self.next("1")

    def text_screen(self):
        print("Developed by EBSouza \n \n")
        print("Pressione [ENTER] para sair")


class StartToPlayScreen(Screen):

    def __init__(self, prev_reference):
        self.id = {"code": "playGame",
                   "reference": self}
        super().__init__()
        self.routes.addRoute("Soma", "1", PlayScreen("1", self.id))
        self.routes.addRoute("Subtração", "2", PlayScreen("2", self.id))
        self.routes.addRoute("Multiplicação", "3", PlayScreen("3", self.id))
        self.routes.addRoute(prev_reference["code"], "4", prev_reference["reference"])

    def text_screen(self):
        print("Modos de jogo \n")


class ExitScreen:

    def print(self):
        os.system("clear")
        print("Obrigado pela sua participação \n \n")
        print("Pressione qualquer tecla para sair")
        input("")
        time.sleep(0.5)
        os.system("clear")
        quit()


class PlayScreen:

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

    def request_input(self):
        c = input("")

        if c.lower() == "sair":
            self.prev_screen["reference"].print()
        else:
            self.execute()
            self.statistics.save_records(self.result["correct"],
                                        self.result["incorrect"],
                                        self.result["duration"])
            time.sleep(5)
            self.prev_screen["reference"].print()

    def execute(self):
        questions = self.generator.generate_question(5)
        self.init_result()

        start_time = time.time()
        for question in questions:
            self.print_question(question)
            self.read_answer(question)
            time.sleep(1)

        self.result["duration"] = time.time() - start_time
        os.system("clear")
        self.print_result()

    def init_result(self):
        self.result = {"correct": 0,
                       "incorrect": 0,
                       "duration": 0}

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
        print("Duração: {:.1f} segundos".format(self.result["duration"]))

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
