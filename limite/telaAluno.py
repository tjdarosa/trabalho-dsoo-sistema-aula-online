

from limite.abstractTela import AbstractTela


class TelaAluno(AbstractTela):
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
            matricula = str(input("Insira a matricula: "))
            nome = str(input("Insira o nome: "))
            idade = int(input("Insira a idade: "))
            return {"nome": nome, "idade": idade, "matricula": matricula}
        except TypeError:
            self.mostra_msg("Insira um valor válido!")
        except Exception:
            self.mostra_msg("Ocorreu um erro ao inserir informações")

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
        matricula = input("Matricula do aluno que deseja selecionar: ")
        return matricula
