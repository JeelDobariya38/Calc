from tokens import Token, TokenType

class Lexer:
    def __init__(self, code):
        self.code = iter(code)
        self.tokens = []
        self.isnum = False

    def iswhitespace(self, letter):
        if letter in "\t \n":
            return True
        return False

    def tokonize(self):
        currtoken = ""

        for letter in self.code:
            if self.iswhitespace(letter):
                if currtoken != "" and self.isnum:
                    token = Token(
                        TokenType.NUMBER,
                        currtoken
                    )
                    self.tokens.append(token)
                    currtoken = ""
                    self.isnum = False

            currtoken += letter

            if letter in "0123456789.":
                self.isnum = True

        if currtoken != "" and self.isnum:
            token = Token(
                TokenType.NUMBER,
                currtoken
            )
            self.tokens.append(token)

        return self.tokens
