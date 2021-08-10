
from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, disciplinas: list) -> None:
        super().__init__(nome, idade, disciplinas)
