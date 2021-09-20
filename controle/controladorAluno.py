

from dao.alunoDAO import AlunoDAO
from entidades.curso import Curso
from entidades.aluno import Aluno
from limite.telaAluno import TelaAluno
from entidades.professor import Professor
from controle.abstractControlador import AbstractControlador


class ControladorAluno(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__aluno_dao = AlunoDAO()
        self.__tela_aluno = TelaAluno()

    @property
    def tela_aluno(self) -> TelaAluno:
        return self.__tela_aluno

    @property
    def alunos(self) -> list:
        return self.__alunos

    def pega_aluno_por_matricula(self, matricula: int):
        for aluno in self.__aluno_dao.getAll():
            if aluno.matricula == matricula:
                return aluno
        return None

    def abre_tela(self):
        try:
            lista_opcoes = {0: self.retornar,
                            1: self.listar_alunos,
                            2: self.inclui_aluno,
                            3: self.altera_aluno,
                            4: self.exclui_aluno}
            while True:
                botao, dados = self.__tela_aluno.open()
                self.__tela_aluno.close()
                lista_opcoes[botao]()
        except KeyError:
            self.__tela_aluno.init_componentes()
            self.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def altera_aluno(self):
        try:
            botao, dados = self.__tela_aluno.seleciona_aluno_para_alterar()
            if botao not in ('cancelar', None):
                aluno = self.pega_aluno_por_matricula(int(dados['matricula']))
                
                if aluno is not None:
                    botao, novos_dados = self.__tela_aluno.pega_novos_dados_aluno()
                    if novos_dados is not None and botao not in ('cancelar', None):
                        if (int(novos_dados["idade"]) > 150) or (int(novos_dados["idade"]) < 0):
                            self.__tela_aluno.showMessage(
                                'ERRO',
                                "ATENÇÃO: Insira um valor numérico entre 0 e 150\n")
                            return None
                        else:
                            # verifica se a matricula já existe.
                            matricula_repetida = False
                            if len(self.__aluno_dao.getAll()) > 0:
                                todos_alunos = self.__aluno_dao.getAll()
                                for aluno in todos_alunos:
                                    if novos_dados['matricula'] == aluno.matricula:
                                        self.__tela_aluno.showMessage(
                                            'ERRO',
                                            'Esta matrícula já está sendo utilizada!')
                                        matricula_repetida = True
                                        break

                            if matricula_repetida == False:
                                aluno_alterado = Aluno(
                                    int(novos_dados['matricula']),
                                    novos_dados['nome'],
                                    int(novos_dados['idade']),
                                    aluno.disciplinas,
                                    aluno.curso)
                                
                                self.__aluno_dao.remove(aluno.matricula)
                                self.__aluno_dao.add(
                                    int(novos_dados['matricula']), aluno_alterado)
                            
                                self.__tela_aluno.showMessage(
                                    'SUCESSO',
                                    'Cadastro do aluno alterado!')
                    else:
                        return None
                else:
                    self.__tela_aluno.showMessage(
                        'ERRO',
                        "ATENÇÃO: Aluno inexistente!")
            else:
                return None
        except ValueError:
            self.__tela_aluno.showMessage(
                'ERRO',
                "Um ou mais valores inseridos não estão corretos!")
        except Exception:
            self.__tela_aluno.showMessage(
                'ERRO',
                "Houve um problema ao alterar o aluno!")

    def exclui_aluno(self):
        try:
            botao, dados = self.__tela_aluno.seleciona_aluno_para_excluir()
            if botao not in ('cancelar', None):
                aluno = self.pega_aluno_por_matricula(int(dados['matricula']))
                if aluno is not None:
                    self.__aluno_dao.remove(aluno.matricula)
                    self.__tela_aluno.showMessage(
                        'SUCESSO',
                        'Aluno de matrícula "{}" foi excluído!\n'.format(dados['matricula']))
                else:
                    self.__tela_aluno.showMessage(
                        'SUCESSO',
                        "ATENÇÃO: Aluno inexistente!")
            else:
                return None
        except Exception:
            self.__tela_aluno.showMessage(
                        'ERRO',
                        "Houve um problema ao excluir aluno!")


    def inclui_aluno(self):
        try:
            # print(botao, dados)
            botao, dados = self.__tela_aluno.pega_dados_aluno()
            if dados is not None and botao not in ('cancelar', None):
                if int(dados["idade"]) > 150 or int(dados["idade"]) < 0:
                    self.__tela_aluno.showMessage(
                        'ERRO',
                        "ATENÇÃO: Insira um valor numérico entre 0 e 150 para a idade!")
                else:
                    # verifica se a matricula já existe.
                    matricula_repetida = False
                    if len(self.__aluno_dao.getAll()) > 0:
                        todos_alunos = self.__aluno_dao.getAll()
                        for aluno in todos_alunos:
                            if int(dados['matricula']) == aluno.matricula:
                                self.__tela_aluno.showMessage(
                                    'ERRO',
                                    'Esta matrícula já está sendo utilizada!')
                                matricula_repetida = True
                                break

                    if not matricula_repetida:
                        novo_aluno = Aluno(int(dados["matricula"]), dados["nome"], dados["idade"], [], Curso('Aluno não matriculado em nenhum curso', [], 'codigo'))
                        self.__aluno_dao.add(int(dados["matricula"]), novo_aluno)
                        self.__tela_aluno.showMessage(
                            'SUCESSO',
                            'Aluno adicionado!')
            else:
                return None
        except ValueError:
            self.__tela_aluno.showMessage(
                'ERRO',
                "Um ou mais valores inseridos não estão corretos!")
        except Exception:
            self.__tela_aluno.showMessage(
                'ERRO',
                "Houve problema ao adicionar aluno!")


    def listar_alunos(self):
        try:
            if len(self.__aluno_dao.getAll()) == 0:
                self.__tela_aluno.showMessage(
                    'ERRO',
                    "Nenhum aluno cadastrado!")
            else:
                alunos = {}
                for aluno in self.__aluno_dao.getAll():
                    disciplinas = []
                    for disciplina in aluno.disciplinas:
                        disciplinas.append(disciplina.nome)
                        
                    alunos[aluno.matricula] = {
                        'idade': aluno.idade,
                        'nome': aluno.nome,
                        'disciplinas': disciplinas,
                        'curso': aluno.curso.nome}
                self.__tela_aluno.mostra_alunos(alunos)
        except Exception:
            self.__tela_aluno.showMessage(
                'ERRO',
                "Houve problema ao listar alunos!")