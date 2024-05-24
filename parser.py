from nodes import *
from tokens import TokenType
from customerr import *

def isnumbernode(node):
    res = str(node.execute())
    for char in res:
        if not char in "1234567890.-":
            return False
    return True

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)

    def get_binary_args(self, parsetree):
        left = None
        right = None

        try:
            left = parsetree.args[-1]
            right = next(self.tokens)
        except StopIteration as _:
            raise InvalidSyntaxError(f"Invalid Syntax!!!")

        if not isnumbernode(left) or right.type != TokenType.NUMBER:
            raise InvalidSyntaxError(f"Adding something of type \"{left.type}\" to \"{right.type}\" is invalid!!!")

        right = NumberNode(data=float(right.data))
        return [left, right]

    def parse(self):
        parsetree = Node()
        for token in self.tokens:
            if token.type == TokenType.NUMBER:
                node = NumberNode(data=float(token.data))
                parsetree.args.append(node)
            elif token.type == TokenType.PLUS:
                args = self.get_binary_args(parsetree)
                node = AddNode(args)
                parsetree.args[-1] = node
            elif token.type == TokenType.OUTPUT:
                outparsetree = self.parse()
                node = OutNode(outparsetree.args)
                parsetree.args.append(node)
        return parsetree
