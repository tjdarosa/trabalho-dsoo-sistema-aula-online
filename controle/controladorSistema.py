

from controle.controladorAtividade import ControladorAtividade
from controle.controladorAluno import ControladorAluno
from controle.controladorProfessor import ControladorProfessor
from controle.controladorDisciplina import ControladorDisciplina
from controle.controladorGerarRelatorio import ControladorGerarRelatorio
from controle.controladorCurso import ControladorCurso
from limite.telaSistema import TelaSistema
from controle.abstractControlador import AbstractControlador


class ControladorSistema(AbstractControlador):
    def __init__(self) -> None:
        self.__tela_sistema = TelaSistema()

        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__controlador_atividade = ControladorAtividade(self)
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_gerar_relatorio = ControladorGerarRelatorio(self)

    @property
    def controlador_disciplina(self) -> ControladorDisciplina:
        return self.__controlador_disciplina

    @property
    def controlador_professor(self) -> ControladorProfessor:
        return self.__controlador_professor

    @property
    def controlador_aluno(self) -> ControladorAluno:
        return self.__controlador_aluno

    @property
    def controlador_curso(self) -> ControladorCurso:
        return self.__controlador_curso

    @property
    def controlador_atividade(self) -> ControladorAtividade:
        return self.__controlador_atividade

    def abre_tela(self) -> None:
        lista_opcoes = {"0 - Sair do Sistemas": self.encerra_sistema,
                        "1 - Gerar Relatórios": self.relatorios,
                        "2 - Cadastro de Cursos": self.cadastra_curso,
                        "3 - Cadastro de Disciplinas": self.cadastra_disciplinas,
                        "4 - Cadastro de Professores": self.cadastra_professores,
                        "5 - Cadastro de Alunos": self.cadastra_aluno,
                        "6 - Cadastro de Atividades": self.cadastra_atividade}
        while True:
            button, values = self.__tela_sistema.open()
            # opcao_escolhida = self.__tela_sistema.mostra_opcoes()
            self.__tela_sistema.close()
            lista_opcoes[button]()

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_disciplinas(self):
        self.__controlador_disciplina.abre_tela()

    def cadastra_professores(self):
        self.__controlador_professor.abre_tela()

    def cadastra_aluno(self):
        self.__controlador_aluno.abre_tela()

    def cadastra_atividade(self):
        self.__controlador_atividade.abre_tela()

    def cadastra_curso(self):
        self.__controlador_curso.abre_tela()

    def relatorios(self):
        self.__controlador_gerar_relatorio.abre_tela()

    def encerra_sistema(self):
        exit(0)
