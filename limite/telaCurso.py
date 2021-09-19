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
        return self.open()

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

    def mostra_opcoes_old(self):
        print("=========== CADASTROS DE CURSOS ===========")
        print('Escolha a opção: ')
        print("1 - Listar Cursos")
        print("2 - Adicionar Cursos")
        print("3 - Alterar Cursos")
        print("4 - Excluir Cursos")
        print("0 - Retornar")
        while True:
            try:
                opcao = int(input('Escolha uma opção: '))
                print()
                if opcao > 4 or opcao < 0:
                    raise Exception
                return opcao
            except TypeError:
                print('Insira um número válido.')
                continue
            except Exception:
                print('Insira um valor numérico entre 0 e 4.')
                continue

    def pega_nome_qtd_disciplinas_curso(self) -> dict:
        try:
            nome = str(input("Insira o nome do curso: "))
            numero_disciplinas = int(
                input('informe quantas disciplinas terá o curso:'))

            return {'nome': nome, 'qtd_disciplinas': numero_disciplinas}
        except TypeError:
            self.mostra_msg("Insira um nome ou valor válido!")
            self.pega_nome_qtd_disciplinas_curso
        except Exception:
            self.pega_nome_qtd_disciplinas_curso

    def pega_disciplinas_curso(self, qtd_disciplinas) -> list:
        try:
            count = 0
            disciplinas = []
            while count < qtd_disciplinas:
                disciplina = str(input('Insira o nome da ' +
                                 str(count + 1) + 'a' + ' disciplina:'))
                disciplinas.append(disciplina)
                count += 1
            return disciplinas
        except TypeError:
            self.mostra_msg("Insira um nome válido!")
        except Exception:
            self.mostra_msg("Ocorreu um erro ao inserir informações")

    def mostra_curso(self, curso):
        print("NOME:", curso.nome)
        print("DISCIPLINAS:")
        for disciplina in curso.disciplinas:
            print(disciplina)
        print("\n")

    def seleciona_curso(self):
        try:
            nome = input("Nome do curso que deseja selecionar: ")
            return nome
        except Exception:
            self.mostra_msg('Houve um erro na inserção de informações!\n')

    def mostra_msg(self, msg):
        print(msg)
