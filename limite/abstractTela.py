
from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def showMessage(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
