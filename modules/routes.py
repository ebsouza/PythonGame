# -*- coding: utf-8 -*-

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