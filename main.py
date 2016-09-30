# coding=UTF-8

from printScreen import printScreen
from roundGame import roundGame

#Instantiates the object screen
screen = printScreen()
#Stores the user choose
choose = 0
#Main loop
while choose != 2:
    #Initial screen
    choose = screen.initialScreen()

    #Start gameplay
    if (choose == 1):
        #Instantiates the object gameplay
        game = roundGame()
        #Start gameplay
        game.start()
        #Delete the gameplay object
        del game
    else:
        # Display the exit screen
        screen.exitScreen()


