

from dao.abstractDAO import AbstractDAO
from entidades.professor import Professor


class ProfessorDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__('professores.pkl')

    def get(self, key):
        if isinstance(key, int):
            return super().get(key)

    def add(self, id, professor):
        if (professor is not None) and (isinstance(professor, Professor) and (isinstance(id, int))):
            return super().add(id, professor)

    def remove(self, key):
        if isinstance(key, int):
            return super().remove(key)

    def getAll(self):
        return super().getAll()
