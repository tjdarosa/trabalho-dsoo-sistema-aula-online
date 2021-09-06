

from entidades import disciplina, professor
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
            {"nome": aluno.nome, "matricula": aluno.matricula, "idade": aluno.idade, "curso": aluno.curso.nome, "disciplina": disciplinas})

    def relatorio_disciplina(self):
        self.__controlador_sistema.controlador_disciplina.listar_disciplinas()
        nome = self.__tela_gerar_relatorio.seleciona_disciplina_do_relatorio()
        disciplina = self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_nome(
            nome)
        if disciplina is None:
            self.__tela_gerar_relatorio.mostra_msg(
                "ATENÇÃO: Disciplina Inexistente")
            return None

        alunos = []
        for aluno in disciplina.alunos:
            alunos.append(aluno.matricula + " - " + aluno.nome)
        atividades = []
        for atividade in self.__controlador_sistema.controlador_atividade.atividades:
            if atividade.disciplina == disciplina:
                atividades.append(
                    {"titulo": atividade.titulo, "descricao": atividade.descricao, "prazo": atividade.prazo})
        self.__tela_gerar_relatorio.mostra_relatorio_disciplina(
            {"nome": disciplina.nome, "professor": disciplina.professor.nome, "limite_alunos": disciplina.limite_alunos, "alunos": alunos, "atividades": atividades})

    def relatorio_curso(self):
        self.__controlador_sistema.controlador_curso.listar_cursos()
        nome = self.__tela_gerar_relatorio.seleciona_curso_do_relatorio()
        curso = self.__controlador_sistema.controlador_curso.pega_curso_por_nome(
            nome)
        if curso is None:
            self.__tela_gerar_relatorio.mostra_msg(
                "ATENÇÃO: Curso Inexistente")
        disciplinas = []
        professores = []
        alunos = []

        for disciplina_str in curso.disciplinas:
            disciplinas.append(disciplina_str)
            disciplina = None
            for disc in self.__controlador_sistema.controlador_disciplina.disciplinas:
                if disc.nome == disciplina_str:
                    disciplina = disc
            if disciplina.professor not in professores:
                professores.append(disciplina.professor.nome)
            for aluno in disciplina.alunos:
                if aluno not in alunos:
                    alunos.append(aluno.matricula + " - " + aluno.nome)

        self.__tela_gerar_relatorio.mostra_relatorio_curso(
            {"nome": curso.nome, "disciplinas": disciplinas, "alunos": alunos, "professores": professores})

    def retornar(self):
        self.__controlador_sistema.abre_tela()
