# -*- coding: utf-8 -*-

import os
from abc import ABC, abstractmethod


class Routes:
    def __init__(self):
        self.data = list()
        self.options = list()

    def addRoute(self, code, option, reference):
        data = {"code": code, 
                "option": option, 
                "reference": reference}
        self.data.append(data)
        self.updateOptions()

    def updateOptions(self):
        self.options = [i["option"] for i in self.data]

    def getReference(self, option):
        for data in self.data:
            try:
                if data["option"] == option:
                    return data["reference"]
            except KeyError:
                pass
        return None


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