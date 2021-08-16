

from limite.abstractTela import AbstractTela
from datetime import datetime


class TelaAtividade(AbstractTela):
    def mostra_opcoes(self):
        print("=========== CADASTROS DE ATIVIDADES ===========")
        while True:
            try:
                print("Escolha a opção:")
                print("1 - Listar Atividades")
                print("2 - Adicionar Atividade")
                print("3 - Alterar Atividade")
                print("4 - Excluir Atividade")
                print("5 - Adicionar Entrega de Aluno a Atividade")
                print("6 - Avaliar Atividade de Aluno")
                print("7 - Excluir Atividade de Aluno")

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

    def pega_dados_atividade(self):
        print("------------- DADOS ATIVIDADE -------------")
        try:
            titulo = str(input("Insira o título: "))
            descricao = str(input("Insira a Descrição: "))
            prazo = datetime.strptime(
                str(input("Insira o Prazo de Entrega no formato dd/MM/yyyy: ")), "%d/%m/%Y")
            return {"titulo": titulo, "descricao": descricao, "prazo": prazo}
        except TypeError:
            self.mostra_msg("Insira um valor válido!")
        except Exception as err:
            self.mostra_msg(
                "Ocorreu um erro ao inserir informações, verifique novamente os dados inseridos")

    def pega_dados_atividade_aluno(self):
        print("------------- DADOS ATIVIDADE ALUNO -------------")
        try:
            data_entrega = datetime.strptime(
                str(input("Insira a Data de Entrega no formato dd/MM/yyyy: ")))
            return {"data_que_foi_entregue": data_entrega}
        except TypeError:
            self.mostra_msg("Insira um valor válido!")
        except Exception:
            self.mostra_msg("Ocorreu um erro ao inserir informações")

    def mostra_atividade(self, dados_atividade):
        print("TITULO: ", dados_atividade["titulo"])
        print("DESCRIÇÃO: ", dados_atividade["descricao"])
        print("PRAZO ENTREGA: ", dados_atividade["prazo"])
        print("PROFESSOR RESPONSÁVEL: ",
              dados_atividade["professor_responsavel"])
        print("DISCIPLINA: ", dados_atividade["disciplina"])
        print("ENTREGAS: ")
        if len(dados_atividade["atividades_aluno"]) > 0:
            for atividade_aluno in dados_atividade["atividades_aluno"]:
                print(" ALUNO: ", atividade_aluno["nome"])
                print(" DATA DE ENTREGA: ",
                      atividade_aluno["data_que_foi_entregue"])
                print(" NOTA: ", atividade_aluno["nota"])
                print(" STATUS: ", atividade_aluno["status"])
        else:
            print("Nenhuma atividade entregue até o momento")
        print("\n")

    def seleciona_atividade(self):
        nome = str(input("Titulo da Atividade que deseja selecionar: "))
        return nome
