
class Curso:
    def __init__(self, nome: str, disciplinas: list) -> None:
        self.__nome = nome
        self.__disciplinas = disciplinas

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def disciplinas(self) -> list:
        return self.__disciplinas

    @disciplinas.setter
    def disciplinas(self, disciplinas: str) -> None:
        self.__disciplinas = disciplinas
