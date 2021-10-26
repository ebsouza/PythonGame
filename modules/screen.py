# -*- coding: utf-8 -*-

import os
import time
from abc import ABC, abstractmethod

from modules.routes import Routes
from modules.question import Manager


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
        self.routes.addRoute("Jogar", "1", PlayScreen(self.id))
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

    def requestInput(self):
        input("")
        self.next("1")

    def text_screen(self):
        print("Developed by EBSouza \n \n")
        print("Pressione [ENTER] para sair")


class PlayScreen(Screen):

    def __init__(self, prev_reference):
        self.id = {"code": "playGame",
                   "reference": self}
        super().__init__()
        self.routes.addRoute("Soma", "1", Manager("1", self.id))
        self.routes.addRoute("Subtração", "2", Manager("2", self.id))
        self.routes.addRoute("Multiplicação", "3", Manager("3", self.id))
        self.routes.addRoute("Divisão", "4", Manager("4", self.id))
        self.routes.addRoute(prev_reference["code"], "5", prev_reference["reference"])
        self.question = ["1", "2", "3", "4", "5"]

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
