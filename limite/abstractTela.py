
from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):

    def open(self):
        pass

    def close(self):
        pass

    def showMessage(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
