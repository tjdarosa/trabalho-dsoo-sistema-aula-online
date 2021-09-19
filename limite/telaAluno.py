

from limite.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaAluno(AbstractTela):

    def __init__(self) -> None:
        self.__window = None
        self.init_componentes()

    def init_componentes(self):
        layout = [
            [sg.Text('Gerenciamento de Cadastro de Alunos', size=(35,1), font=('Times', 20), justification='c')],
            [sg.Button('Listar Alunos', key=1, size=30)],
            [sg.Button('Adicionar Alunos', key=2, size=30)],
            [sg.Button('Alterar Alunos', key=3, size=30)],
            [sg.Button('Excluir Alunos', key=4, size=30)],
            [sg.Button('Retornar', key=0, size=30)]
        ]
        self.__window = sg.Window('Gerenciamento de Cadastro de Alunos', element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)


    def pega_dados_aluno(self):
        layout = [
            [sg.Text("Insira a matricula:"), sg.InputText('Matrícula (ex:123)', key='matricula')],
            [sg.Text("Insira o nome:"), sg.InputText('Nome', key='nome')],
            [sg.Text("Insira a idade:"), sg.InputText('Idade (ex:34)', key='idade')],
            [sg.Submit(button_text="Confirmar", key='confirmar'), sg.Cancel("Cancelar", key='cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Alunos', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_componentes()
        return botao, dados

    def pega_novos_dados_aluno(self):
        layout = [
            [sg.Text('Insira abaixo os novos dados do aluno:')],
            [sg.Text("Insira a matricula:"), sg.InputText('Matrícula (ex:123)', key='matricula')],
            [sg.Text("Insira o nome:"), sg.InputText('Nome', key='nome')],
            [sg.Text("Insira a idade:"), sg.InputText('Idade (ex:34)', key='idade')],
            [sg.Submit(button_text="Confirmar", key='confirmar'), sg.Cancel("Cancelar", key='cancelar')]
        ]
        self.__window = sg.Window('Alteração de Cadastro de Alunos', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_componentes()
        return botao, dados
    
    def mostra_alunos(self, alunos):
        layout = []
        if alunos == {}:
            layout.append([sg.Text('Não há alunos cadastrados!', size=(35,1), font=('Times', 20), justification='c')])
        else:
            for key, value in alunos.items():
                layout.append([
                    [sg.Text('Matricula:'), sg.Text(str(key))],
                    [sg.Text('Nome:'), sg.Text(str(value['nome']))],
                    [sg.Text('Idade:'), sg.Text(str(value['idade']))],
                    [sg.Text('Curso:'), sg.Text(value['curso'])],
                    [sg.Text('Disciplinas:')]
                ])
                if value['disciplinas'] == []:
                    layout.append(
                    [sg.Text('Aluno não matriculado em nehuma disciplina.')]
                    )
                else:
                    for disciplina in value['disciplinas']:
                        layout.append([sg.Text(str(disciplina))])
                layout.append([sg.Text('')])
                
        layout.append([sg.Button('OK', size=15)])
        self.__window = sg.Window('Listagem de Alunos', element_justification='c').Layout(layout)

    def seleciona_aluno_para_alterar(self):
        layout = [
            [sg.Text('Insira a Matrícula:'), sg.InputText('Matrícula (ex: 123)', key='matricula')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
        ]
        self.__window = sg.Window('Alteração de Cadastro de Alunos', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_componentes()
        return botao, dados

    def seleciona_aluno_para_excluir(self):
        layout = [
            [sg.Text('Insira a Matrícula:'), sg.InputText('Matrícula (ex: 123)', key='matricula')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
        ]
        self.__window = sg.Window('Exclusão de Cadastro de Alunos', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_componentes()
        return botao, dados

    # def mostra_opcoes(self):
    #     print("=========== CADASTROS DE ALUNOS ===========")
    #     while True:
    #         try:
    #             print("Escolha a opção:")
    #             print("1 - Listar Alunos")
    #             print("2 - Adicionar Aluno")
    #             print("3 - Alterar Aluno")
    #             print("4 - Excluir Aluno")
    #             print("0 - Retornar")

    #             opcao = int(input())
    #             if opcao < 0 or opcao > 6:
    #                 raise Exception()
    #             return opcao
    #         except TypeError:
    #             print("Insira um número válido")
    #             continue
    #         except Exception:
    #             print("Insira um número de 1 à 6")
    #             continue

    # def mostra_msg(self, msg: str) -> None:
    #     print(msg)

    # def pega_dados_aluno(self):
    #     try:
    #         matricula = int(input("Insira a matricula: "))
    #         nome = str(input("Insira o nome: "))
    #         idade = int(input("Insira a idade: "))
    #         return {"nome": nome, "idade": idade, "matricula": matricula}
    #     except TypeError:
    #         self.mostra_msg("Insira um valor válido!\n")
    #     except Exception:
    #         self.mostra_msg("Ocorreu um erro na inserção de informações!\n")

    # def mostra_aluno(self, dados_aluno):
    #     print("MATRÍCULA: ", dados_aluno["matricula"])
    #     print("NOME: ", dados_aluno["nome"])
    #     print("IDADE: ", dados_aluno["idade"])
    #     print("DISCIPLINAS:")
    #     if len(dados_aluno["disciplinas"]) == 0:
    #         print("Aluno não matriculado em nenhuma disciplina")
    #     else:
    #         for disciplina in dados_aluno["disciplinas"]:
    #             print(" NOME: ", disciplina["nome"])
    #     print("\n")

    # def seleciona_aluno(self):
    #     try:
    #         matricula = int(
    #             input("Matricula do aluno que deseja selecionar: "))
    #         return matricula
    #     except TypeError:
    #         self.mostra_msg(
    #             'A matrícula deve conter apenas números inteiros!\n')
    #     except Exception:
    #         self.mostra_msg('Houve um erro na inserção de informações!\n')
