

from dao.abstractDAO import AbstractDAO
from entidades.curso import Curso


class CursoDAO(AbstractDAO):
    def __init__(self) -> None:
        super().__init__("cursos.pkl")

    def add(self, curso: Curso):
        if curso is not None and isinstance(curso, Curso):
            super().add(curso.codigo, curso)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def update(self, curso: Curso):
        if (curso is not None) and isinstance(curso, Curso) and isinstance(curso.codigo, str):
            super().update(curso.codigo, curso)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
