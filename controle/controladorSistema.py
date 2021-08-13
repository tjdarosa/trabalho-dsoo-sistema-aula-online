

from limite.telaSistema import TelaSistema
from controle.abstractControlador import AbstractControlador


class ControladorSistema(AbstractControlador):
    def __init__(self) -> None:
        self.__tela_sistema = TelaSistema()

        # self.__controlador_aluno = ControladorAluno(self)
        # self.__controlador_curso = ControladorCurso(self)
        # self.__controlador_disciplina = ControladorDisciplina(self)
        # self.__controlador_atividade = ControladorAtividade(self)
        # self.__controlador_professor = ControladorProfessor(self)
        # self.__controlador_gerar_relatorio = ControladorGerarRelatorio(self)

    def abre_tela(self) -> None:

        opcao_escolhida = self.__tela_sistema.mostra_opcoes()
        print("OPÇÂO")

    def inicializa_sistema(self):
        self.abre_tela()
