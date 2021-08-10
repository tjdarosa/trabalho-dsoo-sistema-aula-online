
from abc import ABC, abstractmethod


class AbstractTela(ABC):

    @abstractmethod
    def mostra_opcoes(self):
        pass
