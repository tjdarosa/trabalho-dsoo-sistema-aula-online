

from abstractTela import AbstractTela


class TelaSistema(AbstractTela):

    def mostra_opcoes(self):
        print("=========== SISTEMA DE GERENCIAMENTO DE AULAS ONLINE ===========")
        while True:
            try:
                print("Escolha a opção:")
                print("1 - Gerar Relatórios")
                print("2 - Cadastro de Cursos")
                print("3 - Cadastro de Disciplinas")
                print("4 - Cadastro de Professores")
                print("5 - Cadastro de Alunos")
                print("6 - Cadastro de Atividades")
                print("0 - Sair do Sistema")

                opcao = int(input())
                if opcao < 0 or opcao > 6:
                    raise Exception()
                return opcao
            except TypeError:
                print("Insira um número válido")
                continue
            except Exception as error:
                print("Insira um número de 1 à 6")
                continue
