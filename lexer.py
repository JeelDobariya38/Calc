from tokens import Token, TokenType


class Lexer:
    def __init__(self, code):
        self.code = iter(code)
        self.tokens = []
        self.isnum = False
        self.currtoken = ""

    def iswhitespace(self, letter):
        if letter in "\t \n":
            return True
        return False

    def gettoken(self):
        if self.currtoken == "+":
            return Token(TokenType.PLUS, None)

        if self.currtoken.lower() == "out":
            return Token(TokenType.OUTPUT, None)

    def tokonize(self):
        for letter in self.code:
            if self.iswhitespace(letter):
                if self.currtoken != "" and self.isnum:
                    token = Token(
                        TokenType.NUMBER,
                        self.currtoken
                    )
                    self.tokens.append(token)
                    self.currtoken = ""
                    self.isnum = False
                continue

            if letter in "0123456789.-":
                if self.currtoken == "":
                    self.isnum = True
            else:
                if self.isnum:
                    self.isnum = False

            self.currtoken += letter

            token = self.gettoken()
            if token:
                self.tokens.append(token)
                self.currtoken = ""
                continue

        if self.currtoken != "" and self.isnum:
            token = Token(
                TokenType.NUMBER,
                self.currtoken
            )
            self.tokens.append(token)

        return self.tokens
