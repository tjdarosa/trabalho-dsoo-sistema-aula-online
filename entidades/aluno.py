
from pessoa import Pessoa
from curso import Curso


class Aluno(Pessoa):
    def __init__(self, matricula: str, nome: str, idade: int, disciplinas: list, curso: Curso) -> None:
        super().__init__(nome, idade, disciplinas)
        self.__matricula = matricula
        self.__curso = curso

    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str) -> None:
        self.__matricula = matricula

    @property
    def curso(self) -> Curso:
        return self.__curso

    @curso.setter
    def curso(self, curso: str) -> None:
        self.__curso = curso
