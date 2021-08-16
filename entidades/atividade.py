
from entidades.disciplina import Disciplina
from entidades.professor import Professor
from datetime import date as Date


class Atividade:
    def __init__(self, titulo: str, descricao: str, prazo: Date, professor_responsavel: Professor, atividades_aluno: list, disciplina: Disciplina) -> None:
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prazo = prazo
        self.__professor_responsavel = professor_responsavel
        self.__atividades_aluno = atividades_aluno
        self.__disciplina = disciplina

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self.__descricao = descricao

    @property
    def prazo(self) -> Date:
        return self.__prazo

    @prazo.setter
    def prazo(self, prazo: Date) -> None:
        self.__prazo = prazo

    @property
    def professor_responsavel(self) -> Professor:
        return self.__professor_responsavel

    @professor_responsavel.setter
    def professor_responsavel(self, professor_responsavel: Professor) -> None:
        self.__professor_responsavel = professor_responsavel

    @property
    def atividades_aluno(self) -> list:
        return self.__atividades_aluno

    @atividades_aluno.setter
    def atividades_aluno(self, atividades_aluno: list) -> None:
        self.__atividades_aluno = atividades_aluno

    @property
    def disciplina(self) -> Disciplina:
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, disciplina: Disciplina) -> None:
        self.__disciplina = disciplina
