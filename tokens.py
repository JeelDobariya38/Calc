from enum import Enum
from typing import Any
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = "Num"
    PLUS = "Plus"
    MINUS = "Minus"
    MULTIPLE = "Multiple"
    DIVIDE = "Divide"
    OUTPUT = "Out"
    LPRAM = "LPram"
    RPRAM = "RPram"


@dataclass
class Token:
    type: TokenType
    data: Any = None
