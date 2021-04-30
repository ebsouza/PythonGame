from modules.screen import Screen


user_choice = 0
options = {
    "exit": "3",
    "play": "1",
    "credits": "2"
}

while user_choice != options["exit"]:
    
    user_choice = Screen.main()

    if user_choice == options["play"]:
        while user_choice != "6":
            user_choice = Screen.playGame()
            if user_choice == "1":
                print("Iniciando soma")
            if user_choice == "2":
                print("Iniciando subtração")
            if user_choice == "3":
                print("Iniciando multiplicação")
            if user_choice == "4":
                print("Iniciando divisão")
            if user_choice == "5":
                print("Iniciando misto")

    elif user_choice == options["credits"]:
        user_choice = Screen.credits()


Screen.clear()
print("Obrigado por jogar Python Game.")
