

from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, idade: int, disciplinas: list) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__disciplinas = disciplinas

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self.__idade = idade

    @property
    def disciplinas(self) -> list:
        return self.__disciplinas

    @disciplinas.setter
    def disciplinas(self, disciplinas: list) -> None:
        self.__disciplinas = disciplinas
