# coding=UTF-8

from os import system
import re

#Class that print in the screen
class printScreen:

    #Constructor
    def __init__(self):
        self.resetScreen()

    #Initial screen
    def initialScreen(self):
        print ' ------ Seja bem vindo ao Perguntas de Matemática ------'
        print '    '
        print '    '
        print ' Escolha uma das opções abaixo para navegar no jogo '
        print ' --------------------------------------------------- '
        print '    '
        print ' - Digite 1 para iniciar uma partida'
        print ' - Digite 2 para sair do programa'
        print '    '
        print ' --------------------------------------------------- '

        #User choose
        validInput = False
        pattern = r"^[0-9]$"
        while (not validInput):
            choose = raw_input()
            if re.match(pattern, choose):
                validInput = True
            else:
                print 'Entrada invalida'

        #Reset the screen display
        self.resetScreen()
        return int(choose)

    #Gameplay header
    def printHeader(self,right,wrong,round):
        print '--------------------------------------'
        print '| Acertos: '+ str(right) + ' / Erros: ' + str(wrong) + ' / Round: ' + str(round) + ' |'
        print '--------------------------------------'
        print '                   '

    #Question
    def printQuestion(self,a,b):
        print '---------------------------'
        print '|          ' + str(a) +' x '+ str(b) + '          |'
        print '---------------------------'

    #End game message
    def endGame(self, duration):
        #Transformar segundos em minutos quando necessário !!!
        print '                         '
        print ' ----- Tempo de jogo : ' + str(duration) + ' segundos -----'
        print '                         '
        print ' Você perdeu. Aperte qualquer tecla para continuar'
        raw_input()
        self.resetScreen()

    #Exit screen
    def exitScreen(self):
        self.resetScreen()
        print 'Obrigado !'

    def invalidEnter(self):
        print 'Opção inválida'
        print '    '

    #Reset screen action
    def resetScreen(self):
        system("clear")