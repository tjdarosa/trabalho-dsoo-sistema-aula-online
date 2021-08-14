

from limite.abstractTela import AbstractTela


class TelaDisciplina(AbstractTela):
    def mostra_opcoes(self):
        print("=========== CADASTROS DE DISCIPLINAS ===========")
        while True:
            try:
                print("Escolha a opção:")
                print("1 - Listar Disciplinas")
                print("2 - Adicionar Disciplina")
                print("3 - Alterar Disciplina")
                print("4 - Excluir Disciplina")
                print("5 - Adicionar Aluno à Disciplina")
                print("6 - Excluir Aluno de Disciplina")
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

    def pega_dados_disciplina(self):
        print("------------- DADOS DISCIPLINA -------------")
        try:
            nome = str(input("Insira o nome: "))
            limite_alunos = int(input("Insira o limite de alunos: "))
            return {"nome": nome, "limite_alunos": limite_alunos}
        except TypeError:
            self.mostra_msg("Insira um valor válido!")
        except Exception:
            self.mostra_msg("Ocorreu um erro ao inserir informações")

    def mostra_disciplina(self, dados_disciplina):
        print("NOME: ", dados_disciplina["nome"])
        print("LIMITE ALUNOS: ", dados_disciplina["limite_alunos"])
        print("PROFESSOR: ", dados_disciplina["professor"])
        print("ALUNOS:")
        if len(dados_disciplina["alunos"]) == 0:
            print("Nenhum aluno matriculado nesta disciplina")
        else:
            for aluno in dados_disciplina["alunos"]:
                print(" MATRÍCULA: ", aluno["matricula"])
                print(" NOME: ", aluno["nome"])
        print("\n")

    def seleciona_disciplina(self):
        nome = str(input("Nome da disciplina que deseja selecionar: "))
        return nome
