

from controle.abstractControlador import AbstractControlador
from controle.controladorDisciplina import ControladorDisciplina
from limite.telaGerarRelatorio import TelaGerarRelatorio


class ControladorGerarRelatorio(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_gerar_relatorio = TelaGerarRelatorio()

    def abre_tela(self):
        lista_opcoes = {0: self.retornar,
                        1: self.relatorio_curso,
                        2: self.relatorio_disciplina,
                        3: self.relatorio_aluno}
        while True:
            lista_opcoes[self.__tela_gerar_relatorio.mostra_opcoes()]()

    def relatorio_aluno(self):
        self.__controlador_sistema.controlador_aluno.listar_alunos()
        matricula = self.__tela_gerar_relatorio.seleciona_aluno_do_relatorio()
        aluno = self.__controlador_sistema.controlador_aluno.pega_aluno_por_matricula(
            matricula)
        if(aluno is None):
            self.__tela_gerar_relatorio.mostra_msg(
                "ATENÇÃO: Aluno Inexistente")
            return None
        disciplinas = []
        for dic in aluno.disciplinas:
            disciplinas.append(dic.nome)
        self.__tela_gerar_relatorio.mostra_relatorio_aluno(
            {"nome": aluno.nome, "matricula": aluno.matricula, "idade": aluno.idade, "curso": "Sistemas de Informação", "disciplina": disciplinas})

    def relatorio_disciplina(self):
        pass

    def relatorio_curso(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()
