
from datetime import date as Date
from entidades.aluno import Aluno


class AtividadeAluno:
    def __init__(self, data_que_foi_entregue: Date, nota: float, aluno: Aluno, status: str) -> None:
        self.__data_que_foi_entregue = data_que_foi_entregue
        self.__nota = nota
        self.__aluno = aluno
        self.__status = status

    @property
    def data_que_foi_entregue(self) -> Date:
        return self.__data_que_foi_entregue

    @data_que_foi_entregue.setter
    def data_que_foi_entregue(self, data_que_foi_entregue: Date) -> None:
        self.__data_que_foi_entregue = data_que_foi_entregue

    @property
    def nota(self) -> float:
        return self.__nota

    @nota.setter
    def nota(self, nota: float) -> None:
        self.__nota = nota

    @property
    def aluno(self) -> Aluno:
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno: Aluno) -> None:
        self.__aluno = aluno

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        self.__status = status
