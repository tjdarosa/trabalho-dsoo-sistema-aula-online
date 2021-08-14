

from entidades.professor import Professor


class Disciplina:
    def __init__(self, nome: str, alunos: list, professor: Professor, limite_alunos: int) -> None:
        self.__nome = nome
        self.__alunos = alunos
        self.__professor = professor
        self.__limite_alunos = limite_alunos

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def alunos(self) -> list:
        return self.__alunos

    @alunos.setter
    def alunos(self, alunos: list) -> None:
        self.__alunos = alunos

    @property
    def professor(self) -> Professor:
        return self.__professor

    @professor.setter
    def professor(self, professor: Professor) -> None:
        self.__professor = professor

    @property
    def limite_alunos(self) -> int:
        return self.__limite_alunos

    @limite_alunos.setter
    def limite_alunos(self, limite_alunos: int) -> None:
        self.__limite_alunos = limite_alunos
