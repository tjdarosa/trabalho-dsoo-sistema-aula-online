

from dao.abstractDAO import AbstractDAO
from entidades.aluno import Aluno


class AlunoDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('alunos.pkl')

    def get(self, key):
        if isinstance(key, int):
            return super().get(key)

    def add(self, matricula, aluno):
        if (aluno is not None) and (isinstance(aluno, Aluno) and (isinstance(matricula, int))):
            return super().add(matricula, aluno)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)

    def getAll(self):
        return super().getAll()
