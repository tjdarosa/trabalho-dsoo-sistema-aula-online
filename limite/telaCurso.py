from limite.abstractTela import AbstractTela
#from controle.controladorCurso import ControladorCurso
from controle.controladorDisciplina import ControladorDisciplina


class TelaCurso(AbstractTela):
    
    def mostra_opcoes(self):
        print("=========== CADASTROS DE CURSOS ===========")
        print('Escolha a opção: ')
        print("1 - Listar Cursos")
        print("2 - Adicionar Cursos")
        print("3 - Alterar Cursos")
        print("4 - Excluir Cursos")
        print("0 - Retornar")
        while True:
            try:
                opcao = int(input('Escolha uma opção: '))
                print()
                if opcao > 4 or opcao < 0:
                    raise Exception
                return opcao
            except TypeError:
                print('Insira um número válido.')
                continue
            except Exception:
                print('Insira um valor numérico entre 0 e 4.')
                continue
        

    def pega_nome_qtd_disciplinas_curso(self) -> dict:
        try:
            nome = str(input("Insira o nome do curso: "))
            numero_disciplinas = int(input('informe quantas disciplinas terá o curso:'))
            print()
            
            return {'nome': nome, 'qtd_disciplinas': numero_disciplinas}
        except TypeError:
            self.mostra_msg("Insira um nome ou valor válido!")
            self.pega_nome_qtd_disciplinas_curso
        except Exception:
            self.pega_nome_qtd_disciplinas_curso

    def pega_disciplinas_curso(self, qtd_disciplinas) -> list:
        try:
            count = 0
            disciplinas = []
            while count < qtd_disciplinas:
                    disciplina = str(input('Insira o nome da ' + str(count + 1) + 'a' + ' disciplina:'))
                    disciplinas.append(disciplina)
                    count += 1
            return disciplinas
        except TypeError:
            self.mostra_msg("Insira um nome válido!")
        except Exception:
            self.mostra_msg("Ocorreu um erro ao inserir informações")

    def mostra_curso(self, dados_curso):
        print("NOME: ", dados_curso["nome"])
        print("DISCIPLINAS: ")
        for disciplina in dados_curso['disciplinas']:
            print(disciplina)
        print("\n")

    def seleciona_curso(self):
        nome = input("Nome do curso que deseja selecionar: ")
        return nome

    def mostra_msg(self, msg):
        print(msg)
    