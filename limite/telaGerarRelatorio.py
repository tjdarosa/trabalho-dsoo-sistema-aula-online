from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import Self
from entidades.curso import Curso
from entidades.professor import Professor
from limite.abstractTela import AbstractTela
#from controle.controladorGerarRelatorio import ControladorGerarRelatorio
from controle.controladorAluno import ControladorAluno
import PySimpleGUI as sg


class TelaGerarRelatorio(AbstractTela):
    def __init__(self) -> None:
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Gerenciamento de Cadastro de Professores', size=(35,1), font=('Times', 20), justification='c')],
            [sg.Button('Gerar Relatório de Curso', key=1, size=30)],
            [sg.Button('Gerar Relatório de Disciplina', key=2, size=30)],
            [sg.Button('Gerar Relatório de Aluno', key=3, size=30)],
            [sg.Button('Retornar', key=0, size=30)]
        ]

        self.__window = sg.Window('Geração de Relatórios', element_justification='c').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def showMessage(self, titulo: str, mensagem: str):
        return super().showMessage(titulo, mensagem)



    # def mostra_opcoes(self):

    #     print("=========== GERAR RELATÓRIOS ===========")
    #     print('Escolha a opção:')
    #     print('1 - Gerar relatório de curso')
    #     print('2 - Gerar relatório de disciplina')
    #     print('3 - Gerar relatório de aluno')
    #     print('0 - Retornar')

    #     while True:
    #         try:
    #             opcao = int(input('Escolha uma opção: '))
    #             if opcao > 3 or opcao < 0:
    #                 raise Exception
    #             return opcao
    #         except TypeError:
    #             print('Insira um número válido!\n')
    #             continue
    #         except Exception:
    #             print('Insira um valor numérico entre 0 e 3!\n.')
    #             continue

    # def seleciona_curso_do_relatorio(self):
    #     try:
    #         curso_do_relatorio = str(input(
    #             'Informe o curso que deseja obter relatório: '))
    #         return curso_do_relatorio
    #     except TypeError:
    #         print('Informe um nome válido!')
    #         self.seleciona_curso_do_relatorio()
    #     except Exception:
    #         print('Houve um problema ao informar o curso.')
    #         self.seleciona_curso_do_relatorio()

    # def seleciona_disciplina_do_relatorio(self):
    #     try:
    #         disciplina_do_relatorio = str(input(
    #             'Informe o Nome da Disciplina que deseja obter relatório: '))
    #         return disciplina_do_relatorio
    #     except TypeError:
    #         print('Informe um nome válido!')
    #         self.seleciona_disciplina_do_relatorio()
    #     except Exception:
    #         print('Houve um problema ao informar a disciplina.')
    #         self.seleciona_disciplina_do_relatorio()

    # def seleciona_aluno_do_relatorio(self):
    #     try:
    #         matr_aluno_do_relatorio = int(input(
    #             'Informe a matricula do Aluno que deseja obter relatório: '))
    #         return matr_aluno_do_relatorio
    #     except TypeError:
    #         print('Informe uma matrícula válida!')
    #         self.seleciona_aluno_do_relatorio()
    #     except Exception:
    #         print('Houve um problema ao informar o aluno.')
    #         self.seleciona_aluno_do_relatorio()

    # def mostra_relatorio_curso(self, dados_curso):
    #     print('NOME DO CURSO: ', dados_curso['nome'])
    #     print('DISCIPLINAS: ')
    #     if(len(dados_curso["disciplinas"]) == 0):
    #         print("Nenhuma disciplina ligada a este Curso.\n")
    #     else:
    #         for disciplina in dados_curso['disciplinas']:
    #             print(disciplina)
    #     print("PROFESSORES:")
    #     if(len(dados_curso["professores"]) == 0):
    #         print("Nenhum professor dando aula neste curso.\n")
    #     else:
    #         for professor in dados_curso['professores']:
    #             print(professor)
    #     print("ALUNOS:")
    #     if(len(dados_curso["alunos"]) == 0):
    #         print("Nenhum aluno matriculado neste curso.\n")
    #     else:
    #         for aluno in dados_curso['alunos']:
    #             print(aluno)

    # def mostra_relatorio_disciplina(self, dados_disciplina):
    #     print('NOME DA DISCIPLINA: ', dados_disciplina['nome'])
    #     print('PROFESSOR DA DISCIPLINA: ', dados_disciplina['professor'])
    #     print('LIMITE DE ALUNOS DA DISCIPLINA: ',
    #           dados_disciplina['limite_alunos'])
    #     print('ALUNOS DA DISCIPLINA: ')
    #     if(len(dados_disciplina["alunos"]) == 0):
    #         print("Nenhum aluno matriculado nesta disciplina")
    #     else:
    #         for aluno in dados_disciplina['alunos']:
    #             print(aluno)
    #     print("ATIVIDADES DA DISCIPLINA:")
    #     if(len(dados_disciplina["atividades"]) == 0):
    #         print("Nenhuma atividade criada nesta disciplina")
    #     else:
    #         for atividade in dados_disciplina['atividades']:
    #             print(" TITULO: "+atividade["titulo"])
    #             print(" DESCRIÇÃO: "+atividade["descricao"])
    #             print(" PRAZO: " + atividade["prazo"])

    # def mostra_relatorio_aluno(self, dados_aluno):
    #     print('NOME DO ALUNO: ', dados_aluno['nome'])
    #     print('MATRÍCULA DO ALUNO: ', dados_aluno['matricula'])
    #     print('IDADE DO ALUNO: ', dados_aluno['idade'])
    #     print('CURSO DO ALUNO: ', dados_aluno['curso'])
    #     print('DISCIPLINAS DO ALUNO: ')
    #     if len(dados_aluno["disciplina"]) == 0:
    #         print("Aluno não matriculado em nenhuma disciplina")
    #     else:
    #         for disciplina in dados_aluno['disciplina']:
    #             print(disciplina)

    # def mostra_msg(self, msg):
    #     print(msg)
