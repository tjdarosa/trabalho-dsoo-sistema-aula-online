

from entidades.atividade import Atividade
from limite.telaAtividade import TelaAtividade
from entidades.curso import Curso
from entidades.aluno import Aluno
from controle.abstractControlador import AbstractControlador


class ControladorAtividade(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__atividades = []
        self.__tela_atividade = TelaAtividade()

    @property
    def tela_atividade(self) -> TelaAtividade:
        return self.__tela_atividade

    def pega_atividade_por_titulo(self, titulo: str):
        for atividade in self.__atividades:
            if atividade.titulo == titulo:
                return atividade
        return None

    def abre_tela(self):
        lista_opcoes = {0: self.retornar,
                        1: self.listar_atividades,
                        2: self.inclui_atividade, 
                        3: self.altera_atividade, 
                        4: self.exclui_atividade}
        while True:
            lista_opcoes[self.__tela_atividade.mostra_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def altera_atividade(self):
        self.listar_atividades()
        titulo = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo)

        if atividade is not None:
            novos_dados = self.__tela_atividade.pega_dados_atividade()
            if novos_dados is None:
                return None
            self.__tela_atividade.mostra_msg("SELECIONE UM PROFESSOR:")
            professor = self.pega_professor_pra_disciplina()
            if(professor is None):
                self.__tela_atividade.mostra_msg(
                    "ATENÇÃO: Professor não identificado, não foi possível adicionar atividade")
                return None
            self.__tela_atividade.mostra_msg("SELECIONE UMA DISCIPLINA:")
            disciplina = self.pega_disciplina_pra_atividade()
            if(disciplina is None):
                self.__tela_atividade.mostra_msg(
                    "ATENÇÃO: Disciplina não identificada, não foi possível adicionar atividade")
                return None
            atividade.titulo = novos_dados["titulo"]
            atividade.descricao = novos_dados["descricao"]
            atividade.prazo = novos_dados["prazo"]
            atividade.professor_responsavel = professor
            atividade.disciplina = disciplina
            self.listar_atividades()
        else:
            self.__tela_atividade.mostra_msg(
                "ATENÇÃO: Atividade inexistente")

    def exclui_atividade(self):
        self.listar_atividades()
        titulo = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo)
        if atividade is not None:
            self.__atividades.remove(atividade)
            self.listar_atividades()
        else:
            self.__tela_atividade.mostra_msg(
                "ATENÇÃO: Atividade inexistente")

    def inclui_atividade(self):
        dados = self.__tela_atividade.pega_dados_atividade()
        if dados is None:
            return None
        self.__tela_atividade.mostra_msg("SELECIONE UM PROFESSOR:")
        professor = self.pega_professor_pra_atividade()
        if(professor is None):
            self.__tela_atividade.mostra_msg(
                "ATENÇÃO: Professor não identificado, não foi possível adicionar atividade")
            return None

        self.__tela_atividade.mostra_msg("SELECIONE UMA DISCIPLINA:")
        disciplina = self.pega_disciplina_pra_atividade()
        if(disciplina is None):
            self.__tela_atividade.mostra_msg(
                "ATENÇÃO: Disciplina não identificada, não foi possível adicionar atividade")
            return None

        self.__atividades.append(
            Atividade(dados["titulo"], dados["descricao"], dados["prazo"], professor, [], disciplina))

    def listar_atividades(self):
        if len(self.__atividades) == 0:
            self.__tela_atividade.mostra_msg("Nenhuma Atividade cadastrado")
        else:
            for atividade in self.__atividades:
                atividades_aluno = []
                for atividade_aluno in atividade.atividades_aluno:
                    atividades_aluno.append(
                        {"nome": atividade_aluno.aluno.nome, 
                        "data_que_foi_entregue": atividade_aluno.data_que_foi_entregue, 
                        "nota": atividade_aluno.nota, 
                        "status": atividade_aluno.status})
                self.__tela_atividade.mostra_atividade(
                    {"titulo": atividade.titulo, 
                    "descricao": atividade.descricao, 
                    "prazo": atividade.prazo, 
                    "professor_responsavel": atividade.professor_responsavel.nome, 
                    "disciplina": atividade.disciplina.nome, 
                    "atividades_aluno": atividades_aluno})

    def pega_professor_pra_atividade(self):
        self.__controlador_sistema.controlador_professor.listar_professores()
        nome = self.__controlador_sistema.controlador_professor.tela_professor.seleciona_professor()
        return self.__controlador_sistema.controlador_professor.pega_professor_por_nome(nome)

    def pega_disciplina_pra_atividade(self):
        self.__controlador_sistema.controlador_disciplina.listar_disciplinas()
        nome = self.__controlador_sistema.controlador_disciplina.tela_disciplina.seleciona_disciplina()
        return self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_nome(nome)
