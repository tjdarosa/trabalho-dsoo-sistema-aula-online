

from PySimpleGUI.PySimpleGUI import Cancel, InputText
from limite.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaDisciplina(AbstractTela):
    def __init__(self) -> None:
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Gerenciamento de Cadastro de Disciplinas', size=(
                35, 1), font=('Times', 20), justification='c')],
            [sg.Button('Listar Disciplinas', key=1, size=30)],
            [sg.Button('Adicionar Disciplina', key=2, size=30)],
            [sg.Button('Alterar Disciplina', key=3, size=30)],
            [sg.Button('Excluir Disciplina', key=4, size=30)],
            [sg.Button('Adicionar Aluno a Disciplina', key=5, size=30)],
            [sg.Button('Excluir Aluno da Disciplina', key=6, size=30)],
            [sg.Button('Retornar', key=0, size=30)]
        ]

        self.__window = sg.Window(
            'Gerenciamento de Cadastro de disciplinas', element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        return super().showMessage(titulo, mensagem)

    def mostra_disciplina(self, dados_disciplina: dict):
        layout = []
        if dados_disciplina == {}:
            layout.append([sg.Text('Não há disciplinas cadastradas!', size=(
                35, 1), font=('Times', 20), justification='c')])
        else:
            for key in dados_disciplina.keys():
                layout.append(
                    [sg.Text('Disciplina:'), sg.Text(str(key))],
                    [sg.Text('Limite de Alunos:'), sg.Text(
                        str(key['limite_alunos']))]
                    # continuar com demais dados depois de testar
                )
        layout.append([sg.OK(size=15)])
        self.__window = sg.Window(
            'Listagem de Disciplinas', element_justification='c').Layout(layout)

    def pega_dados_disciplina(self):
        layout = [
            [sg.Text('Insira o nome:'), sg.InputText(
                'Nome da disiplina', key='nome')],
            [sg.Text('Insira o Código:'), sg.InputText(
                'Código da Disciplina', key='codigo')],
            [sg.Text('Insira o limite de alunos:'), sg.InputText(
                'Limite de alunos', key="limite_alunos")],
            [sg.Text('Insira o professor:'), sg.InputText(
                'Professor da disciplina', key="codigo_professor"), ],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window(
            'Criação de Disciplinas', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_components()
        print(botao, dados)
        return botao, dados

    # def mostra_opcoes(self):
    #     print("=========== CADASTROS DE DISCIPLINAS ===========")
    #     while True:
    #         try:
    #             print("Escolha a opção:")
    #             print("1 - Listar Disciplinas")
    #             print("2 - Adicionar Disciplina")
    #             print("3 - Alterar Disciplina")
    #             print("4 - Excluir Disciplina")
    #             print("5 - Adicionar Aluno à Disciplina")
    #             print("6 - Excluir Aluno de Disciplina")
    #             print("0 - Retornar")

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

    # def mostra_msg(self, msg: str) -> None:
    #     print(msg)

    # def pega_dados_disciplina(self):
    #     print("------------- DADOS DISCIPLINA -------------")
    #     try:
    #         nome = str(input("Insira o nome: "))
    #         limite_alunos = int(input("Insira o limite de alunos: "))
    #         return {"nome": nome, "limite_alunos": limite_alunos}
    #     except TypeError:
    #         self.mostra_msg("Insira um valor válido!\n")
    #     except Exception:
    #         self.mostra_msg("Ocorreu um erro na inserção de informações!\n")

    # def mostra_disciplina(self, dados_disciplina):
    #     print("NOME: ", dados_disciplina["nome"])
    #     print("LIMITE ALUNOS: ", dados_disciplina["limite_alunos"])
    #     print("PROFESSOR: ", dados_disciplina["professor"])
    #     print("ALUNOS:")
    #     if len(dados_disciplina["alunos"]) == 0:
    #         print("Não há nenhum aluno matriculado nesta disciplina.\n")
    #     else:
    #         for aluno in dados_disciplina["alunos"]:
    #             print(" MATRÍCULA: ", aluno["matricula"])
    #             print(" NOME: ", aluno["nome"])
    #     print("\n")

    # def seleciona_disciplina(self):
    #     try:
    #         nome = str(input("Nome da disciplina que deseja selecionar: "))
    #         return nome
    #     except Exception:
    #         self.mostra_msg('Houve um erro na inserção de informações!\n')
