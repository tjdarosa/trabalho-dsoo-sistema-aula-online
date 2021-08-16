from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import Self
from entidades.curso import Curso
from entidades.professor import Professor
from limite.abstractTela import AbstractTela
#from controle.controladorGerarRelatorio import ControladorGerarRelatorio
from controle.controladorAluno import ControladorAluno


class TelaGerarRelatorio(AbstractTela):

    def mostra_opcoes(self):

        print("=========== GERAR RELATÓRIOS ===========")
        print('Escolha a opção:')
        print('1 - Gerar relatório de curso')
        print('2 - Gerar relatório de disciplina')
        print('3 - Gerar relatório de aluno')
        print('0 - Retornar')

        while True:
            try:
                opcao = int(input('Escolha uma opção: '))
                if opcao > 3 or opcao < 0:
                    raise Exception
                return opcao
            except TypeError:
                print('Insira um numero válido.')
                continue
            except Exception:
                print('Insira um valor numérico entre 0 e 3.')
                continue

    def seleciona_curso_do_relatorio(self):
        try:
            curso_do_relatorio = input(
                'Informe o curso que deseja obter relatório: ')
            if isinstance(curso_do_relatorio, str) == False:
                raise TypeError
        except TypeError:
            print('Informe um nome válido!')
            self.seleciona_curso_do_relatorio()
        except Exception:
            print('Houve um problema ao informar o curso.')
            self.seleciona_curso_do_relatorio()

    def seleciona_disciplina_do_relatorio(self):
        try:
            disciplina_do_relatorio = input(
                'Informe o curso que deseja obter relatório: ')
            if isinstance(disciplina_do_relatorio, str) == False:
                raise TypeError
        except TypeError:
            print('Informe um nome válido!')
            self.seleciona_disciplina_do_relatorio()
        except Exception:
            print('Houve um problema ao informar a disciplina.')
            self.seleciona_disciplina_do_relatorio()

    def seleciona_aluno_do_relatorio(self):
        try:
            aluno_do_relatorio = input(
                'Informe a matricula do Aluno que deseja obter relatório: ')
            if isinstance(aluno_do_relatorio, str) == False:
                raise TypeError
            return aluno_do_relatorio
        except TypeError:
            print('Informe um nome válido!')
            self.seleciona_aluno_do_relatorio()
        except Exception:
            print('Houve um problema ao informar o aluno.')
            self.seleciona_aluno_do_relatorio()

    def mostra_relatorio_curso(self, dados_curso):
        print('NOME DO CURSO: ', dados_curso['nome'])
        print('DISCIPLINAS: ')
        for disciplina in dados_curso['disciplinas']:
            print(disciplina)

    def mostra_relatorio_disciplina(self, dados_disciplina):
        print('NOME DA DISCIPLINA: ', dados_disciplina['nome'])
        print('PROFESSOR DA DISCIPLINA: ', dados_disciplina['professor'])
        print('LIMITE DE ALUNOS DA DISCIPLINA: ',
              dados_disciplina['limite_alunos'])
        print('ALUNOS DA DISCIPLINA: ')
        for aluno in dados_disciplina['alunos']:
            print(aluno)

    def mostra_relatorio_aluno(self, dados_aluno):
        print('NOME DO ALUNO: ', dados_aluno['nome'])
        print('MATRÍCULA DO ALUNO: ', dados_aluno['matricula'])
        print('IDADE DO ALUNO: ', dados_aluno['idade'])
        print('CURSO DO ALUNO: ', dados_aluno['curso'])
        print('DISCIPLINAS DO ALUNO: ')
        if len(dados_aluno["disciplina"]) == 0:
            print("Aluno não matriculado em nenhuma disciplina")
        else:
            for disciplina in dados_aluno['disciplina']:
                print(disciplina)

    def mostra_msg(self, msg):
        print(msg)
