

from limite.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaAluno(AbstractTela):

    def __init__(self) -> None:
        self.__window = None
        self.init_componentes()

    def init_componentes(self):
        layout = [
            [sg.Text("Alunos",
                     size=(30, 1), font=('Times', 25))],
            [sg.Button("Listar Alunos")],
            [sg.Button("Adicionar Aluno")],
            [sg.Button("Alterar Aluno")],
            [sg.Button("Excluir Aluno")],
            [sg.Button("Retornar")],
        ]
        self.__window = sg.Window(
            "Cadastros de Alunos", default_element_size=(50, 1)).Layout(layout)

    def init_inclui_aluno(self):
        layout = [
            [sg.Text("Incluir Aluno",
                     size=(30, 1), font=('Times', 25))],
            [sg.Text("Matricula"), sg.InputText('matricula')],
            [sg.Text("Nome"), sg.InputText('nome')],
            [sg.Text("Idade"), sg.InputText('idade')],
        ]
        self.__window = sg.Window(
            "incluir Aluno", default_element_size=(50, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    def mostra_opcoes(self):
        print("=========== CADASTROS DE ALUNOS ===========")
        while True:
            try:
                print("Escolha a opção:")
                print("1 - Listar Alunos")
                print("2 - Adicionar Aluno")
                print("3 - Alterar Aluno")
                print("4 - Excluir Aluno")
                print("0 - Retornar")

                opcao = int(input())
                if opcao < 0 or opcao > 6:
                    raise Exception()
                return opcao
            except TypeError:
                print("Insira um número válido")
                continue
            except Exception:
                print("Insira um número de 1 à 6")
                continue

    def mostra_msg(self, msg: str) -> None:
        print(msg)

    def pega_dados_aluno(self):
        try:
            matricula = int(input("Insira a matricula: "))
            nome = str(input("Insira o nome: "))
            idade = int(input("Insira a idade: "))
            return {"nome": nome, "idade": idade, "matricula": matricula}
        except TypeError:
            self.mostra_msg("Insira um valor válido!\n")
        except Exception:
            self.mostra_msg("Ocorreu um erro na inserção de informações!\n")

    def mostra_aluno(self, dados_aluno):
        print("MATRÍCULA: ", dados_aluno["matricula"])
        print("NOME: ", dados_aluno["nome"])
        print("IDADE: ", dados_aluno["idade"])
        print("DISCIPLINAS:")
        if len(dados_aluno["disciplinas"]) == 0:
            print("Aluno não matriculado em nenhuma disciplina")
        else:
            for disciplina in dados_aluno["disciplinas"]:
                print(" NOME: ", disciplina["nome"])
        print("\n")

    def seleciona_aluno(self):
        try:
            matricula = int(input("Matricula do aluno que deseja selecionar: "))
            return matricula
        except TypeError:
            self.mostra_msg('A matrícula deve conter apenas números inteiros!\n')
        except Exception:
            self.mostra_msg('Houve um erro na inserção de informações!\n')