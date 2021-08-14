

from controle.controladorProfessor import ControladorProfessor
from controle.controladorDisciplina import ControladorDisciplina
from limite.telaSistema import TelaSistema
from controle.abstractControlador import AbstractControlador


class ControladorSistema(AbstractControlador):
    def __init__(self) -> None:
        self.__tela_sistema = TelaSistema()

        # self.__controlador_aluno = ControladorAluno(self)
        # self.__controlador_curso = ControladorCurso(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        # self.__controlador_atividade = ControladorAtividade(self)
        self.__controlador_professor = ControladorProfessor(self)
        # self.__controlador_gerar_relatorio = ControladorGerarRelatorio(self)

    @property
    def controlador_disciplina(self) -> ControladorDisciplina:
        return self.__controlador_disciplina

    @property
    def controlador_professor(self) -> ControladorProfessor:
        return self.__controlador_professor

    def abre_tela(self) -> None:
        lista_opcoes = {3: self.cadastra_disciplinas,
                        0: self.encerra_sistema, 4: self.cadastra_professores}
        while True:
            opcao_escolhida = self.__tela_sistema.mostra_opcoes()
            lista_opcoes[opcao_escolhida]()

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_disciplinas(self):
        self.__controlador_disciplina.abre_tela()

    def cadastra_professores(self):
        self.__controlador_professor.abre_tela()

    def encerra_sistema(self):
        exit(0)
