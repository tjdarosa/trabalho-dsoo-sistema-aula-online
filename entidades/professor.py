
from entidades.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, disciplinas: list, id: int) -> None:
        super().__init__(nome, idade, disciplinas)
        self.__id = id

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

