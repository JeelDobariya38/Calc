from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.parsetree = None

    def parse(self):
        return self.parsetree