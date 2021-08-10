

from abc import ABC, abstractmethod


class AbstractControlador(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def abre_tela(self) -> None:
        pass
