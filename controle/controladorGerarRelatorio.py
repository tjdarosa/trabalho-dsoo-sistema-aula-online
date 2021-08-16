

from controle.abstractControlador import AbstractControlador
from controle.controladorDisciplina import ControladorDisciplina
from limite.telaGerarRelatorio import TelaGerarRelatorio


class ControladorGerarRelatorio(AbstractControlador):
    def __init__(self, controlador_sistema, controlador_curso, controlador_disciplina, controlador_aluno) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_gerar_relatorio = TelaGerarRelatorio()
        self.__controlador_curso = controlador_curso
        self.__controlador_disciplina = controlador_disciplina
        self.__controlador_aluno = controlador_aluno

    def abre_tela(self):
        lista_opcoes = {0: self.retornar,
                        1: self.relatorio_curso, 
                        2: self.relatorio_disciplina, 
                        3: self.relatorio_aluno}
        while True:
            lista_opcoes[self.__tela_gerar_relatorio.mostra_opcoes()]()

    def relatorio_aluno(self):
        pass

    def relatorio_disciplina(self):
        pass

    def relatorio_curso(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()
