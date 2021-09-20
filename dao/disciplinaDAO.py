

from dao.abstractDAO import AbstractDAO
from entidades.disciplina import Disciplina


class DisciplinaDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__("disciplinas.pkl")

    def add(self, disciplina: Disciplina):
        if disciplina is not None and isinstance(disciplina, Disciplina):
            super().add(disciplina.codigo, disciplina)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def update(self, disciplina: Disciplina):
        if (disciplina is not None) and isinstance(disciplina, Disciplina) and isinstance(disciplina.codigo, int):
            super().update(disciplina.codigo, disciplina)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(str(key))

    def getAll(self):
        return super().getAll()
