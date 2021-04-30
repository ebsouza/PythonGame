import os
import time

class mainScreen():

    def __init__(self):
        self.id = {"code": "main",  
                   "reference": self}
        self.routes = routes()
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

    def __init__(self, prev):
        self.id = {"code": "credits",  
                   "reference": self}
        self.routes = routes()
        self.routes.addRoute(prev["code"], "1", prev["reference"])

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

    def __init__(self, prev):
        self.id = {"code": "playGame",  
                   "reference": self}
        self.routes = routes()
        self.routes.addRoute("soma", "1", None)
        self.routes.addRoute("subtracao", "2", None)
        self.routes.addRoute(prev["code"], "6", prev["reference"])

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
        print("[5] Misto")
        print("[6] Voltar para tela principal")
        self.requestInput()




class exitScreen():

    def print(self):
        os.system("clear")
        print("Obrigado pela sua participação \n \n")
        print("Pressione qualquer tecla para sair")
        input("")
        time.sleep(1)
        os.system("clear")
        quit()


class routes():
    def __init__(self):
        self.data = []
        self.options = []

    def addRoute(self, code, option, reference):
        data = {"code": code, 
                "option": option, 
                "reference": reference}
        self.data.append(data)
        self.updateOptions()

    def updateOptions(self):
        self.options = [ i["option"] for i in self.data ]

    def getReference(self, option):
        for data in self.data:
            try:
                if data["option"] == option:
                    return data["reference"]
            except KeyError:
                pass
        return None


