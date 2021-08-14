

from limite.abstractTela import AbstractTela


class TelaProfessor(AbstractTela):
    def mostra_opcoes(self):
        print("=========== CADASTROS DE PROFESSORES ===========")
        while True:
            try:
                print("Escolha a opção:")
                print("1 - Listar Professores")
                print("2 - Adicionar Professor")
                print("3 - Alterar Professor")
                print("4 - Excluir Professor")
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

    def pega_dados_professor(self):
        nome = str(input("Insira o nome: "))
        idade = str(input("Insira a idade: "))
        return {"nome": nome, "idade": idade}

    def mostra_professor(self, dados_professor):
        print("NOME: ", dados_professor["nome"])
        print("IDADE: ", dados_professor["idade"])
        print("DISCIPLINAS:")
        if len(dados_professor["disciplinas"]) == 0:
            print("Professor não da aula em nenhuma disciplina")
        else:
            for disciplina in dados_professor["disciplinas"]:
                print(" NOME: ", disciplina["nome"])
        print("\n")

    def seleciona_professor(self):
        nome = input("Nome do professor que deseja selecionar: ")
        return nome
