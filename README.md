# PythonGame(In development)
A simple math game written in python.

## General

This game remembers when we had less than ten years old, when our teacher asked for us the answer of multiplication issues. Now you can back to the past and fix what you used to fail or, if you were good in this, improve your results today :)

I like to code, so I decided code this game to express some ideas and test some algorithms and technologies. Another reason is to have some fun, it’s so cool coding games. Nowadays I’ve no “big planning” for this, I just wanna to code and exercise some skills.


## How to play

In the main window( the first one ) you can choose if you wanna play or exit. If you 
start to feel depressed after run the script, it’s recommended to press key 2 before the damage is permanent. I hope you wanna start, after choose the first option pressing the key 1, you will see the initial instructions. If you understood the instructions, you can press any key and start the game, if not you can write to ebsouza07@gmail.com and share your doubts with me. The game finishes when you miss five or answer a total of twenty questions.

To run this game, execute **python main.py** on terminal.


## About the code

This code use the Oriented Object paradigm, so each class has your own domain in general architecture.

- **gameStatistics**

Nowadays this class only receives and exports some player performance data. A file, named “statistics.csv”, is created to save this information. 

- **printScreen**

Every text printed in the screen is printed by printScreen object if another object prints, this code has a big problem.

- **questionGenerator**

If you wanna generate a question you need to call a questionGenerator object, this need a integer **level** as parameter to generate a question with certain level of difficulty( ranging from 1 to 6 ).

Obs: Recently I add **questionSumGenerator** and **questionSumGenerator** to generate questions of addition and subtraction, respectively.

- **roundGame**

This object is responsible to give you fun, if it doesn’t do this it’s not my fault. This object knows everything about the current gameplay, knows set a question level according to current round and manage the gameplay very well.

## System Requirements

Python 2.7 installed 


