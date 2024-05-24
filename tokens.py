from enum import Enum
from typing import Any
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER = "NUM"
    PLUS = "Plus"
    OUTPUT = "Out"

@dataclass
class Token:
    type: TokenType
    data: Any
