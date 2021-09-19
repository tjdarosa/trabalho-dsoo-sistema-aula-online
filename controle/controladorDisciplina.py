

from entidades.professor import Professor
from entidades.disciplina import Disciplina
from limite.telaDisciplina import TelaDisciplina
from controle.abstractControlador import AbstractControlador


class ControladorDisciplina(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__disciplinas = []
        self.__tela_disciplina = TelaDisciplina()

    @property
    def disciplinas(self) -> list:
        return self.__disciplinas

    def tem_disciplinas(self):
        return len(self.__disciplinas) > 0

    @property
    def tela_disciplina(self) -> TelaDisciplina:
        return self.__tela_disciplina

    def pega_disciplina_por_nome(self, nome: str):
        for disciplina in self.__disciplinas:
            if disciplina.nome == nome:
                return disciplina

        return None

    def pega_disciplina_por_codigo(self, codigo: str):
        for disciplina in self.__disciplinas:
            if disciplina.codigo == codigo:
                return disciplina

        return None

    def abre_tela(self):

        lista_opcoes = {0: self.retornar,
                        1: self.listar_disciplinas,
                        2: self.inclui_disciplina,
                        3: self.altera_disciplina,
                        4: self.exclui_disciplina,
                        5: self.inclui_aluno,
                        6: self.exclui_aluno}
        while True:
            botao, dados = self.tela_disciplina.open()
            self.tela_disciplina.close()
            lista_opcoes[botao]()

    def retornar(self):
        self.__tela_disciplina.close()
        self.__controlador_sistema.abre_tela()

    def altera_disciplina(self):
        nome = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome)
        if disciplina is not None:
            disciplina.professor.disciplinas.remove(disciplina)
            novos_dados = self.__tela_disciplina.pega_dados_disciplina()
            self.__tela_disciplina.mostra_msg("SELECIONE UM PROFESSOR:")
            professor = self.pega_professor_pra_disciplina()
            if professor is not None:
                professor.disciplinas.append(disciplina)
                disciplina.nome = novos_dados["nome"]
                disciplina.limite_alunos = novos_dados["limite_alunos"]
                disciplina.professor = professor
                self.listar_disciplinas()
            else:
                self.__tela_disciplina.mostra_msg(
                    "ATENÇÃO: Professor inexistente")
        else:
            self.__tela_disciplina.mostra_msg(
                "ATENÇÃO: Disciplina inexistente")

    def exclui_disciplina(self):
        self.listar_disciplinas()
        nome = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome)
        if disciplina is not None:
            disciplina.professor.disciplinas.remove(disciplina)
            self.__disciplinas.remove(disciplina)
            self.__tela_disciplina.mostra_msg(
                'Disciplina excluída com sucesso!')
        else:
            self.__tela_disciplina.mostra_msg(
                "ATENÇÃO: Disciplina inexistente")

    def inclui_disciplina(self):
        if(self.__controlador_sistema.controlador_professor.professores_len() == 0):
            self.__tela_disciplina.showMessage(
                "ERRO",
                "ATENÇÃO: Cadastre um Professor para poder adicionar uma disciplina!")
            return None
        button, values = self.__tela_disciplina.pega_dados_disciplina()
        if values is not None:
            for professor in self.__controlador_sistema.controlador_professor.professores:
                if values['codigo_professor'] == str(professor.id):
                    nova_disciplina = Disciplina(
                        values["nome"], [], professor, values["limite_alunos"], values["codigo"])
                    self.__disciplinas.append(nova_disciplina)
                    professor.disciplinas.append(nova_disciplina)
                else:
                    self.__tela_disciplina.showMessage(
                        'ERRO',
                        'Professor não encontrado!')
        else:
            return None

    def pega_professor_pra_disciplina(self):
        self.__controlador_sistema.controlador_professor.listar_professores()
        id = self.__controlador_sistema.controlador_professor.tela_professor.seleciona_professor()
        return self.__controlador_sistema.controlador_professor.pega_professor_por_id(id)

    def listar_disciplinas(self):
        disciplinas = {}
        for disciplina in self.__disciplinas:
            alunos = []
            for aluno in disciplina.alunos:
                alunos.append(
                    {"matricula": aluno.matricula, "nome": aluno.nome})
            disciplinas[disciplina.nome] = {
                "limite_alunos": disciplina.limite_alunos, "professor": disciplina.professor.nome, "alunos": alunos}
        self.__tela_disciplina.mostra_disciplina(disciplinas)

    def inclui_aluno(self):
        # Seleciona Disciplina
        self.listar_disciplinas()
        if len(self.__disciplinas) > 0:
            nome = self.__tela_disciplina.seleciona_disciplina()
            disciplina = self.pega_disciplina_por_nome(nome)
            if(disciplina is None):
                self.__tela_disciplina.mostra_msg(
                    "ATENÇÃO: Disciplina Inexistente")
                return None
            if len(disciplina.alunos) == disciplina.limite_alunos:
                self.__tela_disciplina.mostra_msg(
                    "ATENÇÃO: Esta disciplina já atingiu seu limite de aluno máximo permitido ")
                return None
            # Seleciona Aluno
            self.__controlador_sistema.controlador_aluno.listar_alunos()
            matricula = self.__controlador_sistema.controlador_aluno.tela_aluno.seleciona_aluno()
            aluno = self.__controlador_sistema.controlador_aluno.pega_aluno_por_matricula(
                matricula)
            if(aluno is None):
                self.__tela_disciplina.mostra_msg("ATENÇÃO: Aluno Inexistente")
                return None
            if aluno in disciplina.alunos:
                self.__tela_disciplina.mostra_msg(
                    "ATENÇÃO: Aluno já matriculado nesta disciplina")
                return None
            disciplina.alunos.append(aluno)
            aluno.disciplinas.append(disciplina)
            for curso in self.__controlador_sistema.controlador_curso.cursos:
                if disciplina.nome in curso.disciplinas:
                    aluno.curso = curso
                    break
        else:
            return None

    def exclui_aluno(self):
        # Seleciona Disciplina
        self.listar_disciplinas()
        nome = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_nome(nome)

        if len(disciplina.alunos) > 0:
            if(disciplina is None):
                self.__tela_disciplina.mostra_msg(
                    "ATENÇÃO: Disciplina Inexistente!\n")
                return None
            # Seleciona Aluno
            self.__controlador_sistema.controlador_aluno.listar_alunos()
            matricula = self.__controlador_sistema.controlador_aluno.tela_aluno.seleciona_aluno()
            aluno = self.__controlador_sistema.controlador_aluno.pega_aluno_por_matricula(
                matricula)
            if(aluno is None):
                self.__tela_disciplina.mostra_msg(
                    "ATENÇÃO: Aluno Inexistente!\n")
                return None
            if aluno in disciplina.alunos:
                disciplina.alunos.remove(aluno)
                aluno.disciplinas.remove(disciplina)
            else:
                self.__tela_disciplina.mostra_msg(
                    "ATENÇÃO: Aluno não está matriculado nesta disciplina!\n")
        else:
            self.__tela_disciplina.mostra_msg(
                'Esta disciplina não possui alunos!\n')
