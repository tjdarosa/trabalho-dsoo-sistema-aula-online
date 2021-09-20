

from entidades.atividade import Atividade
from dao.abstractDAO import AbstractDAO


class AtividadeDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__("atividades.pkl")

    def add(self, atividade: Atividade):
        if atividade is not None and isinstance(atividade, Atividade):
            super().add(atividade.codigo, atividade)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def getAll(self):
        return super().getAll()
        