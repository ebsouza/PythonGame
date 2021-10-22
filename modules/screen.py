import os
import time
from modules.routes import Routes
from modules.question import SumGenerator, QUESTION_MAPPER

class mainScreen():

    def __init__(self):
        self.id = {"code": "main",  
                   "reference": self}
        self.routes = Routes()
        self.routes.addRoute("playGame", "1", playScreen(self.id))
        self.routes.addRoute("credits", "2", creditsScreen(self.id))
        self.routes.addRoute("exit", "3", exitScreen())

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


class creditsScreen():

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


class playScreen():

    def __init__(self, prev_reference):
        self.id = {"code": "playGame",  
                   "reference": self}
        self.routes = Routes()
        self.routes.addRoute("iniciar", "1", waitRoomScreen(self.id))
        self.routes.addRoute("iniciar", "2", waitRoomScreen(self.id))
        self.routes.addRoute("iniciar", "3", waitRoomScreen(self.id))
        self.routes.addRoute("iniciar", "4", waitRoomScreen(self.id))
        self.routes.addRoute("iniciar", "5", waitRoomScreen(self.id))
        self.routes.addRoute(prev_reference["code"], "6", prev_reference["reference"])
        self.question = ["1", "2", "3", "4", "5"]

    def requestInput(self):
        c = "--"
        while c not in self.routes.options:
            c = input("")
        self.next(c)

    def next(self, c):
        try:
            nextScreen = self.routes.getReference(c)
            if c in self.question:
                generator = QUESTION_MAPPER[c]
                nextScreen.set_question_generator(generator)
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
        print("[5] Misto")
        print("\n")
        print("[6] Voltar para tela principal")
        self.requestInput()


class waitRoomScreen():

    def __init__(self, prev_reference):
        self.id = {"code": "waitRoom",  
                   "reference": self}
        self.routes = Routes()
        self.routes.addRoute("iniciar", "1", questionScreen(prev_reference))
        self.routes.addRoute(prev_reference["code"], "2", prev_reference["reference"])
        self.question_generator = None

    def set_question_generator(self, question_generator):
        self.question_generator = question_generator

    def requestInput(self):
        c = "--"
        while c not in self.routes.options:
            c = input("")
        self.next(c)

    def next(self, c):
        try:
            nextScreen = self.routes.getReference(c)
            if c == "1":
                #self.question_generator.generate(10)
                questions = self.question_generator.generate(10)
                nextScreen.set_questions(questions)
            nextScreen.print()
        except Exception as e:
            print("Desculpe, ocorreu um erro.")
            print(e)

    def print(self):
        os.system("clear")
        print("Sala de espera \n")
        print("Você está prestes a iniciar uma questão")
        print("[1] Iniciar")
        print("[2] Voltar")
        self.requestInput()


class questionScreen():

    def __init__(self, prev_reference):
        self.routes = Routes()
        self.routes.addRoute(prev_reference["code"], "c", prev_reference["reference"])
        self.questions = list()

    def set_questions(self, questions):
        self.questions = questions

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
        try:
            for question in self.questions:
                print(question)
                self.requestInput()
        except Exception as e:
            print("Desculpe, ocorreu um erro.")
            print(e)


class exitScreen():

    def print(self):
        os.system("clear")
        print("Obrigado pela sua participação \n \n")
        print("Pressione qualquer tecla para sair")
        input("")
        time.sleep(0.5)
        os.system("clear")
        quit()





