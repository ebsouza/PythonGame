# -*- coding: utf-8 -*-

import os
from abc import ABC, abstractmethod

from screen.routes import Routes


class Screen(ABC):

    def __init__(self):
        self.routes = Routes()
        self.show_options = True

    def request_input(self):
        c = "--"
        while c not in self.routes.options:
            c = input("")
        self.next(c)

    def next(self, c):
        try:
            next_screen = self.routes.getReference(c)
            next_screen.print()
        except Exception as e:
            print(f"Desculpe, ocorreu um erro. {e}")

    def print(self):
        os.system("clear")
        self.text_screen()

        if self.show_options:
            for data in self.routes.data:
                print(f"[{data['option']}] - {data['code']} ")

        self.request_input()

    @abstractmethod
    def text_screen(self):
        pass