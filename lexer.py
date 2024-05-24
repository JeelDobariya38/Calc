from tokens import Token

class Lexer:
    def __init__(self, code):
        self.code = iter(code)
        self.tokens = []

    def iswhitespace(self, letter):
        if letter in ["\t", " ", "\n"]:
            return True
        return False

    def tokonize(self):
        for letter in self.code:
            if self.iswhitespace(letter):
                continue
        return self.tokens
