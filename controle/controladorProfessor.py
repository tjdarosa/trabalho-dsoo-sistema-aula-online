

from entidades.professor import Professor
from entidades.disciplina import Disciplina
from limite.telaProfessor import TelaProfessor
from controle.abstractControlador import AbstractControlador


class ControladorProfessor(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__professores = []
        self.__tela_professor = TelaProfessor()

    @property
    def tela_professor(self) -> TelaProfessor:
        return self.__tela_professor

    def pega_professor_por_nome(self, nome: str):
        for professor in self.__professores:
            if professor.nome == nome:
                return professor

        return None

    def abre_tela(self):
        lista_opcoes = {0: self.retornar,
                        1: self.listar_professores, 2: self.inclui_professor, 3: self.altera_professor, 4: self.exclui_professor}
        while True:
            lista_opcoes[self.__tela_professor.mostra_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def altera_professor(self):
        self.listar_professores()
        nome = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_nome(nome)

        if professor is not None:
            novos_dados = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados["nome"]
            professor.idade = novos_dados["idade"]
            self.listar_professores()
        else:
            self.__tela_professor.mostra_msg(
                "ATENÇÃO: Professor inexistente")

    def exclui_professor(self):
        self.listar_professores()
        nome = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_nome(nome)
        if professor is not None:
            self.__professores.remove(professor)
            self.listar_professores()
        else:
            self.__tela_professor.mostra_msg(
                "ATENÇÃO: Professor inexistente")

    def inclui_professor(self):
        dados = self.__tela_professor.pega_dados_professor()
        self.__professores.append(Professor(dados["nome"], dados["idade"], []))

    def listar_professores(self):
        if len(self.__professores) == 0:
            self.__tela_professor.mostra_msg("Nenhum professor cadastrado")
        else:
            for professor in self.__professores:
                disciplinas = []
                for disciplina in professor.disciplinas:
                    disciplinas.append({"nome": disciplina.nome})
                self.__tela_professor.mostra_professor(
                    {"nome": professor.nome, "idade": professor.idade, "disciplinas": disciplinas})

    def professores_len(self) -> int:
        return len(self.__professores)
