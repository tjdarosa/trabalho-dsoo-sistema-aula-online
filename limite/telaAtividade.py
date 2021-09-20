

from limite.abstractTela import AbstractTela
from datetime import datetime
import PySimpleGUI as sg


class TelaAtividade(AbstractTela):
    def __init__(self) -> None:
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Gerenciamento de Cadastro de Atividades', size=(35,1), font=('Times', 20), justification='c')],
            [sg.Button('Listar Atividades', key=1, size=30)],
            [sg.Button('Adicionar Atividade', key=2, size=30)],
            [sg.Button('Alterar Atividade', key=3, size=30)],
            [sg.Button('Excluir Atividade', key=4, size=30)],
            [sg.Button('Adicionar Atividade de Aluno', key=5, size=30)],
            [sg.Button('Adicionar Entrega de Aluno a Atividade', key=6, size=30)],
            [sg.Button('Avaliar Atividade de Aluno', key=7, size=30)],
            [sg.Button('Retornar', key=0, size=30)]
        ]
        self.__window = sg.Window('Gerenciamento de Cadastro de Atividades', element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        return super().showMessage(titulo, mensagem)

    def mostra_atividades(self):
        layout = []

    
    
    
    
    
    
    
    
    
    
    # def mostra_opcoes(self):
    #     print("=========== CADASTROS DE ATIVIDADES ===========")
    #     while True:
    #         try:
    #             print("Escolha a opção:")
    #             print("1 - Listar Atividades")
    #             print("2 - Adicionar Atividade")
    #             print("3 - Alterar Atividade")
    #             print("4 - Excluir Atividade")
    #             print("5 - Adicionar Atividade de Aluno")
    #             print("6 - Adicionar Entrega de Aluno a Atividade")
    #             print("7 - Avaliar Atividade de Aluno")

    #             print("0 - Retornar")

    #             opcao = int(input())
    #             if opcao < 0 or opcao > 7:
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

    # def pega_dados_atividade(self):
    #     print("------------- DADOS ATIVIDADE -------------")
    #     try:
    #         titulo = str(input("Insira o título: "))
    #         descricao = str(input("Insira a Descrição: "))
    #         prazo = datetime.strptime(
    #             str(input("Insira o Prazo de Entrega no formato dd/MM/yyyy: ")), "%d/%m/%Y")
    #         return {"titulo": titulo, "descricao": descricao, "prazo": prazo}
    #     except TypeError:
    #         self.mostra_msg("Insira um valor válido!")
    #     except Exception as err:
    #         self.mostra_msg(
    #             "Ocorreu um erro ao inserir informações, verifique novamente os dados inseridos")

    # def pega_dados_atividade_aluno(self):
    #     try:
    #         data_entrega = datetime.strptime(
    #             str(input("Insira a Data de Entrega no formato dd/MM/yyyy: ")), "%d/%m/%Y")
    #         return {"data_que_foi_entregue": data_entrega}
    #     except TypeError:
    #         self.mostra_msg("Insira um valor válido!")
    #     except Exception:
    #         self.mostra_msg("Ocorreu um erro ao inserir informações")

    # def pega_nota_atividade_aluno(self):
    #     try:
    #         nota = float(
    #             input("Insira a Nota: "))
    #         if(nota > 10 or nota < 0):
    #             print("Insira valores entre 0 e 10")
    #             return None
    #         return {"nota": nota}
    #     except TypeError:
    #         self.mostra_msg("Insira um valor válido!")
    #     except Exception:
    #         self.mostra_msg("Ocorreu um erro ao inserir informações")

    # def mostra_atividade(self, dados_atividade):
    #     print("TITULO: ", dados_atividade["titulo"])
    #     print("DESCRIÇÃO: ", dados_atividade["descricao"])
    #     print("PRAZO ENTREGA: ", dados_atividade["prazo"])
    #     print("PROFESSOR RESPONSÁVEL: ",
    #           dados_atividade["professor_responsavel"])
    #     print("DISCIPLINA: ", dados_atividade["disciplina"])
    #     print("ENTREGAS: ")
    #     if len(dados_atividade["atividades_aluno"]) > 0:
    #         for atividade_aluno in dados_atividade["atividades_aluno"]:
    #             print(" ALUNO: ", atividade_aluno["nome"])
    #             print(" DATA DE ENTREGA: ",
    #                   atividade_aluno["data_que_foi_entregue"])
    #             print(" NOTA: ", atividade_aluno["nota"])
    #             print(" STATUS: ", atividade_aluno["status"])
    #     else:
    #         print("Nenhuma atividade entregue até o momento")
    #     print("\n")

    # def seleciona_atividade(self):
    #     try:
    #         nome = str(input("Titulo da Atividade que deseja selecionar: "))
    #         return nome
    #     except Exception:
    #         self.mostra_msg('Houve um erro na inserção de informações!\n')