import os

class Screen:

    @classmethod
    def main(cls):
        cls.clear()
        print("Seja bem-vindo")
        print("Escolha as opções:")
        print("[1] - Iniciar o jogo ")
        print("[2] - Créditos ")
        print("[3] - Sair ")
        c = input("")
        return c

    @classmethod
    def playGame(cls):
        cls.clear()
        print("Iniciar a partida")
        print("[1] - Soma ")
        print("[2] - Subtração ")
        print("[3] - Multiplicação ")
        print("[4] - Divisão ")
        print("[5] - Misto ")
        print(" -- ")
        print("[6] - Sair ")
        c = input("")
        return c

    @classmethod
    def level(cls):
        cls.clear()
        print("IEscolha o seu nível")
        print("[1] - Iniciante ")
        print("[2] - Intermediário ")
        print("[3] - Avançado ")
        print(" -- ")
        print("[4] - Sair ")
        c = input("")
        return c

    @classmethod
    def credits(cls):
        cls.clear()
        print("Developed by EBSouza")
        c = input("")
        return c

    @staticmethod
    def clear():
        os.system("clear")