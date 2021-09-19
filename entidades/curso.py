
class Curso:
    def __init__(self, nome: str, disciplinas: list, codigo: str) -> None:
        self.__nome = nome
        self.__disciplinas = disciplinas
        self.__codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: str) -> None:
        self.__codigo = codigo

    @property
    def disciplinas(self) -> list:
        return self.__disciplinas

    @disciplinas.setter
    def disciplinas(self, disciplinas: str) -> None:
        self.__disciplinas = disciplinas
