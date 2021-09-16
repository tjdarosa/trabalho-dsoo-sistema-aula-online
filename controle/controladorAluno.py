

from entidades.curso import Curso
from entidades.aluno import Aluno
from limite.telaAluno import TelaAluno
from entidades.professor import Professor
from controle.abstractControlador import AbstractControlador


class ControladorAluno(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__tela_aluno = TelaAluno()

    @property
    def tela_aluno(self) -> TelaAluno:
        return self.__tela_aluno

    @property
    def alunos(self) -> list:
        return self.__alunos

    def pega_aluno_por_matricula(self, matricula: int):
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def abre_tela(self):
        lista_opcoes = {"Retornar": self.retornar,
                        "Listar Alunos": self.listar_alunos, "Adicionar Aluno": self.inclui_aluno, "Alterar Aluno": self.altera_aluno, "Excluir Aluno": self.exclui_aluno}
        event, _ = self.__tela_aluno.open()
        self.__tela_aluno.close()
        while True:
            lista_opcoes[event]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def altera_aluno(self):
        self.listar_alunos()
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)

        if aluno is not None:
            novos_dados = self.__tela_aluno.pega_dados_aluno()
            if novos_dados is not None:
                if (novos_dados is None) or (not isinstance(novos_dados["idade"], int)) or (novos_dados["idade"] > 150 or novos_dados["idade"] < 0):
                    self.__tela_aluno.mostra_msg(
                        "ATENÇÃO: Insira um valor numérico entre 0 e 150\n")
                    return None

                # verifica se a matricula já existe.
                matricula_repetida = False
                if len(self.__alunos) > 0:
                    for aluno in self.__alunos:
                        if novos_dados['matricula'] == aluno.matricula:
                            self.__tela_aluno.mostra_msg(
                                'Esta matrícula já está sendo utilizada!\n')
                            matricula_repetida = True
                            break

                if not matricula_repetida:
                    aluno.nome = novos_dados["nome"]
                    aluno.matricula = novos_dados["matricula"]
                    aluno.idade = novos_dados["idade"]
                    self.__tela_aluno.mostra_msg(
                        'Cadastro do aluno alterado!\n')
            else:
                return None
        else:
            self.__tela_aluno.mostra_msg(
                "ATENÇÃO: Aluno inexistente!\n")

    def exclui_aluno(self):
        self.listar_alunos()
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)
        if aluno is not None:
            self.__alunos.remove(aluno)
            self.__tela_aluno.mostra_msg(
                'Aluno de matrícula "{}" foi excluído!\n'.format(matricula))
        else:
            self.__tela_aluno.mostra_msg(
                "ATENÇÃO: Aluno inexistente")

    def inclui_aluno(self):
        self.__tela_aluno.init_inclui_aluno()
        button, values = self.__tela_aluno.open()

        print(button, values)
        dados = self.__tela_aluno.pega_dados_aluno()
        if dados is not None:
            if (not isinstance(dados["idade"], int)) or (dados["idade"] > 150 or dados["idade"] < 0):
                self.__tela_aluno.mostra_msg(
                    "ATENÇÃO: Insira um valor numérico entre 0 e 150!\n")
                return None

            # verifica se a matricula já existe.
            matricula_repetida = False
            if len(self.__alunos) > 0:
                for aluno in self.__alunos:
                    if dados['matricula'] == aluno.matricula:
                        self.__tela_aluno.mostra_msg(
                            'Esta matrícula já está sendo utilizada!\n')
                        matricula_repetida = True
                        break

            if not matricula_repetida:
                self.__alunos.append(
                    Aluno(dados["matricula"], dados["nome"], dados["idade"], [], Curso('Aluno não matriculado em nenhum curso', []), ))
                self.__tela_aluno.mostra_msg('Aluno adicionado!\n')
        else:
            return None

    def listar_alunos(self):
        if len(self.__alunos) == 0:
            self.__tela_aluno.mostra_msg("Nenhum aluno cadastrado! \n")
            # return -1 é utilizado para evitar geração de relatórios caso não exsitam alunos cadastrados.
            return -1
        else:
            for aluno in self.__alunos:
                disciplinas = []
                for disciplina in aluno.disciplinas:
                    disciplinas.append({"nome": disciplina.nome})
                self.__tela_aluno.mostra_aluno(
                    {"nome": aluno.nome, "idade": aluno.idade, "disciplinas": disciplinas, "matricula": aluno.matricula})
