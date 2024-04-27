import abc
from typing import List

class TransformerModel(abc.ABC):

    def __init__(self) -> None:
        pass

    def generate(self, messages) -> str:
        pass
