from enum import Enum
from typing import Any
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER = "NUM"

@dataclass
class Token:
    type: TokenType
    data: Any
