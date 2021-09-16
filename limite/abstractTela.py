
from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):

    @abstractmethod
    def mostra_opcoes(self):
        pass

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
