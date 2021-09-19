

from limite.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaProfessor(AbstractTela):
    def __init__(self) -> None:
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Gerenciamento de Cadastro de Professores', size=(35,1), font=('Times', 20), justification='c')],
            [sg.Button('Listar Professores', key=1, size=30)],
            [sg.Button('Adicionar Professor', key=2, size=30)],
            [sg.Button('Alterar Professor', key=3, size=30)],
            [sg.Button('Excluir Professor', key=4, size=30)],
            [sg.Button('Retornar', key=0, size=30)]
        ]

        self.__window = sg.Window('Gerenciamento de Cadastro de Professores', element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        return super().showMessage(titulo, mensagem)

    def mostra_professores(self, professores: dict):
        print(professores)
        layout = []
        if professores == {}:
            layout.append([sg.Text('Não há professores cadastrados!', size=(35,1), font=('Times', 20), justification='c')])
        else:
            for key, value in professores.items():
                layout.append([
                    [sg.Text('ID:'), sg.Text(key)],
                    [sg.Text('Nome:'), sg.Text(str(value['nome']))],
                    [sg.Text('Idade:'), sg.Text(str(value['idade']))],
                    [sg.Text('Disciplinas:')]
                ])
                if value['disciplinas'] == []:
                    layout.append(
                    [sg.Text('Professor não leciona em nehuma disciplina.')]
                    )
                else:
                    for disciplina in value['disciplinas']:
                        layout.append([sg.Text(str(disciplina))])
                layout.append([sg.Text('')])
                
        layout.append([sg.Button('OK', size=15)])
        self.__window = sg.Window('Listagem de Professoress', element_justification='c').Layout(layout)
        


    def pega_dados_professor(self):
        layout = [
            [sg.Text('Insira o nome:'), sg.InputText('Nome', key='nome')],
            [sg.Text('Insira o ID:'), sg.InputText('ID (ex: 123)', key='id')],
            [sg.Text('Insira a idade:'), sg.InputText('Idade (ex: 34)', key='idade')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
            ]
        self.__window = sg.Window('Cadastro de Professores', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_components()
        return botao, dados

    def pega_novos_dados_professor(self):
        layout = [
            [sg.Text('Insira abaixo os novos dados do professor:')],
            [sg.Text('Insira o nome:'), sg.InputText('Nome', key='nome')],
            [sg.Text('Insira o ID:'), sg.InputText('ID (ex: 123)', key='id')],
            [sg.Text('Insira a idade:'), sg.InputText('Idade (ex: 34)', key='idade')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
            ]
        self.__window = sg.Window('Alteração de Cadastro de Professores', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_components()
        return botao, dados

    def seleciona_professor_para_alterar(self):
        layout = [
            [sg.Text('Insira o ID:'), sg.InputText('ID (ex: 123)', key='id')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
        ]
        self.__window = sg.Window('Alteração de Cadastro de Professores', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_components()
        return botao, dados

    def seleciona_professor_para_excluir(self):
        layout = [
            [sg.Text('Insira o ID:'), sg.InputText('ID (ex: 123)', key='id')],
            [sg.Submit('Confirmar', key='confirmar'), sg.Cancel('Cancelar', key='cancelar')]
        ]
        self.__window = sg.Window('Exclusão de Cadastro de Professores', element_justification='c').Layout(layout)
        botao, dados = self.open()
        self.close()
        self.init_components()
        return botao, dados




# class TelaProfessor(AbstractTela):
#     def mostra_opcoes(self):
#         print("=========== CADASTROS DE PROFESSORES ===========")
#         while True:
#             try:
#                 print("Escolha a opção:")
#                 print("1 - Listar Professores")
#                 print("2 - Adicionar Professor")
#                 print("3 - Alterar Professor")
#                 print("4 - Excluir Professor")
#                 print("0 - Retornar")

#                 opcao = int(input())
#                 if opcao < 0 or opcao > 6:
#                     raise Exception()
#                 return opcao
#             except TypeError:
#                 print("Insira um número válido")
#                 continue
#             except Exception:
#                 print("Insira um número de 1 à 6")
#                 continue

#     def mostra_msg(self, msg: str) -> None:
#         print(msg)

#     def pega_dados_professor(self):
#         try:
#             nome = str(input("Insira o nome: "))
#             idade = int(input("Insira a idade: "))
#             id = int(input('Insira o id: '))
#             return {"nome": nome, "idade": idade, "id": id}
#         except TypeError:
#             self.mostra_msg("Insira um valor válido!\n")
#         except Exception:
#             self.mostra_msg("Ocorreu um erro na inserção de informações!\n")

#     def mostra_professor(self, dados_professor):
#         print("ID: ", dados_professor["id"])
#         print("NOME: ", dados_professor["nome"])
#         print("IDADE: ", dados_professor["idade"])
#         print("ProfessoresS:")
#         if len(dados_professor["Professoress"]) == 0:
#             print("Professor não dá aula em nenhuma Professores.\n")
#         else:
#             for Professores in dados_professor["Professoress"]:
#                 print(" NOME: ", Professores["nome"])
#         print("\n")

#     def seleciona_professor(self):
#         try:
#             id = int(input("Id do professor que deseja selecionar: "))
#             return id
#         except Exception:
#             self.mostra_msg('houve um erro na inserção de informações!\n')
        
