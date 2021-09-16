

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
        try:
            nome = str(input("Insira o nome: "))
            idade = int(input("Insira a idade: "))
            id = int(input('Insira o id: '))
            return {"nome": nome, "idade": idade, "id": id}
        except TypeError:
            self.mostra_msg("Insira um valor válido!\n")
        except Exception:
            self.mostra_msg("Ocorreu um erro na inserção de informações!\n")

    def mostra_professor(self, dados_professor):
        print("ID: ", dados_professor["id"])
        print("NOME: ", dados_professor["nome"])
        print("IDADE: ", dados_professor["idade"])
        print("DISCIPLINAS:")
        if len(dados_professor["disciplinas"]) == 0:
            print("Professor não dá aula em nenhuma disciplina.")
        else:
            for disciplina in dados_professor["disciplinas"]:
                print(" NOME: ", disciplina["nome"])
        print("\n")

    def seleciona_professor(self):
        id = int(input("Id do professor que deseja selecionar: "))
        return id
