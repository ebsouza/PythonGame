# -*- coding: utf-8 -*-

import os


class Question:

    def __init__(self, alternatives, text):
        self.alternatives = alternatives
        self.text = text

    def __str__(self):
        return self.text

    def __eq__(self, question):
        return self.text == question.text
