# -*- coding: utf-8 -*-

import os
import time

from screen.base import Screen
from screen.longterm import PlayScreen


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
