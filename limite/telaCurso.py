from limite.abstractTela import AbstractTela
#from controle.controladorCurso import ControladorCurso

import PySimpleGUI as sg


class TelaCurso(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_componentes()

    def init_componentes(self):
        layout = [
            [sg.Text("Gerenciamento de Cadastro de Cursos", size=(30, 1), font=(
                'Times', 25), justification='c')],
            [sg.Button("Listar Cursos", key=1, size=30)],
            [sg.Button("Adicionar Cursos", key=2, size=30)],
            [sg.Button("Alterar Cursos", key=3, size=30)],
            [sg.Button("Excluir Cursos", key=4, size=30)],
            [sg.Button("Retornar", key=0, size=30)],
        ]
        self.__window = sg.Window(
            "Cadastro de Cursos", default_element_size=(50, 1), element_justification='c').Layout(layout)

    def pega_dados_curso(self, lista_disciplinas: list):
        disciplinas = []
        for disciplina in lista_disciplinas:
            disciplinas.append([sg.Checkbox(
                disciplina["codigo"] + " - " + disciplina["nome"], key=disciplina["codigo"])])
        layout = [
            [sg.Text("Dados Curso", size=(30, 1), font=(
                'Times', 25), justification='c')],
            [sg.Text("Código:"), sg.InputText(key="codigo")],
            [sg.Text("Nome:"), sg.InputText(key="nome")],
            [sg.Text("Selecione as Disciplinas para este Curso:",)],
            *disciplinas,
            [sg.Submit("Concluir", size=20), sg.Button("Retornar", size=20)],
        ]
        self.__window = sg.Window("Dados Curso").Layout(layout)
        button, values = self.open()
        self.close()
        return button, values

    def mostra_cursos(self, cursos: list):
        cursos_rows = []
        for curso in cursos:
            cursos_rows.append([sg.Text("Nome: " + curso["nome"])])
            cursos_rows.append([sg.Text("Código: " + curso["codigo"])])
            cursos_rows.append([sg.Text("Disciplinas do Curso: ")])
            for disciplina in curso["disciplinas"]:
                cursos_rows.append(
                    [sg.Text("   " + disciplina["codigo"] + " - " + disciplina["nome"])])
            cursos_rows.append([sg.Text("\n")])
        layout = [
            [sg.Text("Listagem de Cursos", size=(30, 1), font=(
                'Times', 25), justification='c')],
            *cursos_rows,
            [sg.Button("Voltar")]
        ]

        self.__window = sg.Window("Listagem de Cursos").Layout(layout)
        button, values = self.open()
        self.close()
        return button, values

    def seleciona_curso(self, cursos):
        cursos_rows = []
        for curso in cursos:
            cursos_rows.append(
                [sg.Radio(curso["codigo"]+" - "+curso["nome"], "RADIO_CURSO", key=curso["codigo"])])

        layout = [
            [sg.Text("Selecionar Curso", size=(30, 1), font=(
                'Times', 25), justification='c')],
            *cursos_rows,
            [sg.Submit("Próximo"), sg.Button("Voltar")]
        ]
        self.__window = sg.Window("Selecionar Curso").Layout(layout)
        button, values = self.open()
        self.close()
        return button, values

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def mostra_opcoes(self):
        self.init_componentes()
        button, values = self.open()
        self.close()
        return button, values

    def mostra_msg(self, msg):
        print(msg)
