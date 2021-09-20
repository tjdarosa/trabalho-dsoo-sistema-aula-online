

from limite.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_componentes()

    def init_componentes(self):
        # sg.ChangeLookAndFeel("Reddit")
        layout = [
            [sg.Text("Sistema de Gerenciamento de Aulas Online",
                     size=(35,1), font=('Times', 20), justification='c')],
            [sg.Button("1 - Gerar Relatórios", size=30)],
            [sg.Button("2 - Cadastro de Cursos", size=30)],
            [sg.Button("3 - Cadastro de Disciplinas", size=30)],
            [sg.Button("4 - Cadastro de Professores", size=30)],
            [sg.Button("5 - Cadastro de Alunos", size=30)],
            [sg.Button("6 - Cadastro de Atividades", size=30)],
            [sg.Button("0 - Sair do Sistemas", size=30)]
        ]
        self.__window = sg.Window(
            "Tela Inicial", default_element_size=(40, 1), element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    # def mostra_opcoes(self):
    #     print("=========== SISTEMA DE GERENCIAMENTO DE AULAS ONLINE ===========")
    #     while True:
    #         try:
    #             print("Escolha a opção:")
    #             print("1 - Gerar Relatórios")
    #             print("2 - Cadastro de Cursos")
    #             print("3 - Cadastro de Disciplinas")
    #             print("4 - Cadastro de Professores")
    #             print("5 - Cadastro de Alunos")
    #             print("6 - Cadastro de Atividades")
    #             print("0 - Sair do Sistema")

    #             opcao = int(input())
    #             if opcao < 0 or opcao > 6:
    #                 raise Exception()
    #             return opcao
    #         except TypeError:
    #             print("Insira um número válido!\n")
    #             continue
    #         except Exception:
    #             print("Insira um número de 0 à 6!\n")
    #             continue
