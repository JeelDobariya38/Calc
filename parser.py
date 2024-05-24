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
        self.parsetree = Node()

    def get_binary_args(self):
        left = None
        right = None

        # Left arg
        try:
            left = self.parsetree.args[-1]
            right = next(self.tokens)
        except:
            raise InvalidSyntaxError(f"Invalid Syntax!!!")

        if not isnumbernode(left) or right.type != TokenType.NUMBER:
            raise InvalidSyntaxError(f"Adding something of type \"{left.type}\" to \"{right.type}\" is invalid!!!")

        right = NumberNode(data=float(right.data))
        return [left, right]

    def parse(self):
        for token in self.tokens:
            if token.type == TokenType.NUMBER:
                node = NumberNode(data=float(token.data))
                self.parsetree.args.append(node)
            if token.type == TokenType.PLUS:
                args = self.get_binary_args()
                node = AddNode(args)
                self.parsetree.args[-1] = node
        return self.parsetree
