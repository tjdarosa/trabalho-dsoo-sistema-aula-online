

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

    def pega_aluno_por_matricula(self, matricula: str):
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def abre_tela(self):
        lista_opcoes = {0: self.retornar,
                        1: self.listar_alunos, 2: self.inclui_aluno, 3: self.altera_aluno, 4: self.exclui_aluno}
        while True:
            lista_opcoes[self.__tela_aluno.mostra_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def altera_aluno(self):
        self.listar_alunos()
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)

        if aluno is not None:
            novos_dados = self.__tela_aluno.pega_dados_aluno()
            if(novos_dados["idade"] > 150 or novos_dados["idade"] < 0):
                self.__tela_aluno.mostra_msg(
                    "ATENÇÃO: Insira uma idade entre 0 e 150 anos")
                return None
            aluno.nome = novos_dados["nome"]
            aluno.matricula = novos_dados["matricula"]
            aluno.idade = novos_dados["idade"]
            self.listar_alunos()
        else:
            self.__tela_aluno.mostra_msg(
                "ATENÇÃO: Aluno inexistente")

    def exclui_aluno(self):
        self.listar_alunos()
        matricula = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula)
        if aluno is not None:
            self.__alunos.remove(aluno)
            self.listar_alunos()
        else:
            self.__tela_aluno.mostra_msg(
                "ATENÇÃO: Aluno inexistente")

    def inclui_aluno(self):
        dados = self.__tela_aluno.pega_dados_aluno()
        if(dados["idade"] > 150 or dados["idade"] < 0):
            self.__tela_aluno.mostra_msg(
                "ATENÇÃO: Insira uma idade entre 0 e 150 anos")
            return None
        self.__alunos.append(
            Aluno(dados["matricula"], dados["nome"], dados["idade"], [], Curso("Sistemas de Informação", []), ))

    def listar_alunos(self):
        if len(self.__alunos) == 0:
            self.__tela_aluno.mostra_msg("Nenhum aluno cadastrado")
        else:
            for aluno in self.__alunos:
                disciplinas = []
                for disciplina in aluno.disciplinas:
                    disciplinas.append({"nome": disciplina.nome})
                self.__tela_aluno.mostra_aluno(
                    {"nome": aluno.nome, "idade": aluno.idade, "disciplinas": disciplinas, "matricula": aluno.matricula})
