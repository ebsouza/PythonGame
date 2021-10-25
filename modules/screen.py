import os
import time
from modules.routes import Routes
from modules.question import Manager


class MainScreen:

    def __init__(self):
        self.id = {"code": "main",  
                   "reference": self}
        self.routes = Routes()
        self.routes.addRoute("playGame", "1", PlayScreen(self.id))
        self.routes.addRoute("credits", "2", CreditsScreen(self.id))
        self.routes.addRoute("exit", "3", ExitScreen())

    def requestInput(self):
        c = "--"
        while c not in self.routes.options:
            c = input("")
        self.next(c)

    def next(self, c):
        try:
            nextScreen = self.routes.getReference(c)
            nextScreen.print()
        except Exception as e:
            print("Desculpe, ocorreu um erro.")
            print(e)

    def print(self):
        os.system("clear")
        print("Seja bem-vindo")
        print("Escolha as opções:")
        print("[1] - Iniciar o jogo ")
        print("[2] - Créditos ")
        print("[3] - Sair ")

        self.requestInput()


class CreditsScreen:

    def __init__(self, prev_reference):
        self.id = {"code": "credits",  
                   "reference": self}
        self.routes = Routes()
        self.routes.addRoute(prev_reference["code"], "1", prev_reference["reference"])

    def requestInput(self):
        input("")
        self.next("1")

    def next(self, c):
        try:
            nextScreen = self.routes.getReference(c)
            nextScreen.print()
        except Exception as e:
            print("Desculpe, ocorreu um erro.")
            print(e)

    def print(self):
        os.system("clear")
        print("Developed by EBSouza \n \n")
        print("Pressione [ENTER] para sair")
        self.requestInput()


class PlayScreen:

    def __init__(self, prev_reference):
        self.id = {"code": "playGame",  
                   "reference": self}
        self.routes = Routes()
        self.routes.addRoute("iniciar", "1", Manager("1", self.id))
        self.routes.addRoute("iniciar", "2", Manager("2", self.id))
        self.routes.addRoute("iniciar", "3", Manager("3", self.id))
        self.routes.addRoute("iniciar", "4", Manager("4", self.id))
        self.routes.addRoute(prev_reference["code"], "5", prev_reference["reference"])
        self.question = ["1", "2", "3", "4", "5"]

    def requestInput(self):
        c = "--"
        while c not in self.routes.options:
            c = input("")
        self.next(c)

    def next(self, c):
        try:
            nextScreen = self.routes.getReference(c)
            nextScreen.print()
        except Exception as e:
            print("Desculpe, ocorreu um erro.")
            print(e)

    def print(self):
        os.system("clear")
        print("Modos de jogo \n")
        print("[1] Soma")
        print("[2] Subtração")
        print("[3] Multiplicação")
        print("[4] Divisão")
        print("\n")
        print("[5] Voltar para tela principal")
        self.requestInput()


class ExitScreen:

    def print(self):
        os.system("clear")
        print("Obrigado pela sua participação \n \n")
        print("Pressione qualquer tecla para sair")
        input("")
        time.sleep(0.5)
        os.system("clear")
        quit()





