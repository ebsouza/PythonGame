import os

class mainScreen():

    def __init__(self):
        self.next = {}
        self.code = "main"
        self.routes = {"playGame": ("1",),
                       "credits": ("2",),
                       "exit": ("3",)}
        self.options = self.getOptions()

    def getOptions(self):
        options = [ i[0] for i in self.routes.values() ]
        return options

    def requestInput(self):
        c = "X"
        while c not in self.options:
            c = input("")
        self.getNext(c)

    def getNext(self, c):
        try:
            self.next[c].print()
        except KeyError:
            prev = (self.code, self)
            if c == self.routes["exit"][0]:
                self.next[c] = exitScreen()
            elif c == self.routes["credits"][0]:
                self.next[c] = creditsScreen(prev)
            elif c == self.routes["playGame"][0]:
                self.next[c] = playScreen(prev)
        self.next[c].print()

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
        self.next = {}
        self.routes = {"main": "1"}
        self.options = self.getOptions()
        self.solvePrev(prev)

    def solvePrev(self, prev):
        choice = self.routes[prev[0]]
        self.next[choice] = prev[1]

    def getOptions(self):
        options = [ i for i in self.routes.values() ]
        return options

    def requestInput(self):
        c = input("")
        while c not in self.options:
            c = input("")
        self.getNext(c)

    def getNext(self, c):
        try:
            self.next[c].print()
        except KeyError:
            os.system("clear")
            print("Um erro ocorreu")
            quit()
        self.next[c].print()

    def print(self):
        os.system("clear")
        print("Developed by EBSouza")
        self.requestInput()


class exitScreen():

    def print(self):
        os.system("clear")
        print("Obrigado pela sua participação \n \n")
        print("Pressione qualquer tecla para sair")
        input("")
        quit()


class routes():
    def __init__(self, code, option, reference):
        self.code = code
        self.option = option
        self.reference = reference
