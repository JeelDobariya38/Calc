from enum import Enum
from typing import Any

class TokenType(Enum):
    pass

class Token:
    type: TokenType
    data: Any
