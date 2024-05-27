def add_brackets(expression):
    return expression


def add_space_where_needed(expression):
    return expression


class Filter:
    def __init__(self, expression):
        self.expression = expression

    def apply(self):
        expression = self.expression
        expression = add_brackets(expression)
        expression = add_space_where_needed(expression)
        return expression