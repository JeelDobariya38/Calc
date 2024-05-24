from nodes import *
from tokens import TokenType

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.parsetree = Node()

    def parse(self):
        for token in self.tokens:
            if token.type == TokenType.NUMBER:
                node = NumberNode(float(token.data))
                self.parsetree.args.append(node)
        return self.parsetree
