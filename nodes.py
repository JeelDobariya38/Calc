from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
    args: List = field(default_factory=list)

    def execute(self):
       last_res = 0
       for node in self.args:
           last_res = node.execute()
       return last_res

@dataclass
class NumberNode:
    data: float

    def execute(self):
        return self.data
