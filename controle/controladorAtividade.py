

from entidades.atividadeAluno import AtividadeAluno
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

    @property
    def atividades(self) -> list:
        return self.__atividades

    def pega_atividade_por_titulo(self, titulo: str):
        for atividade in self.__atividades:
            if atividade.titulo == titulo:
                return atividade
        return None

    def abre_tela(self):
        try:
            lista_opcoes = {0: self.retornar,
                            1: self.listar_atividades,
                            2: self.inclui_atividade,
                            3: self.altera_atividade,
                            4: self.exclui_atividade,
                            5: self.inclui_atividade_aluno,
                            6: self.entrega_atividade_aluno,
                            7: self.avalia_atividade_aluno}
            while True:
                    botao, dados = self.__tela_atividade.open()
                    self.__tela_atividade.close()
                    lista_opcoes[botao]()
        except KeyError:
            # print(botao, dados)
            self.__tela_atividade.init_components()
            self.abre_tela()

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
            self.__tela_atividade.showMessage("SELECIONE UM PROFESSOR:")
            professor = self.pega_professor_pra_disciplina()
            if(professor is None):
                self.__tela_atividade.showMessage(
                    "ATENÇÃO: Professor não identificado, não foi possível adicionar atividade")
                return None
            self.__tela_atividade.showMessage("SELECIONE UMA DISCIPLINA:")
            disciplina = self.pega_disciplina_pra_atividade()
            if(disciplina is None):
                self.__tela_atividade.showMessage(
                    "ATENÇÃO: Disciplina não identificada, não foi possível adicionar atividade")
                return None
            atividade.titulo = novos_dados["titulo"]
            atividade.descricao = novos_dados["descricao"]
            atividade.prazo = novos_dados["prazo"]
            atividade.professor_responsavel = professor
            atividade.disciplina = disciplina
            self.listar_atividades()
        else:
            self.__tela_atividade.showMessage(
                "ATENÇÃO: Atividade inexistente")

    def exclui_atividade(self):
        self.listar_atividades()
        titulo = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo)
        if atividade is not None:
            self.__atividades.remove(atividade)
            self.listar_atividades()
        else:
            self.__tela_atividade.showMessage(
                "ATENÇÃO: Atividade inexistente")

    def inclui_atividade(self):
        disciplinas = []
        for disc in self.__controlador_sistema.controlador_disciplina.disciplina_dao.getAll():
            disciplinas.append(disc.nome)
        professores = []
        for prof in self.__controlador_sistema.controlador_professor.professor_dao.getAll():
            professores.append(prof.nome)
        botao, dados = self.__tela_atividade.pega_dados_atividade(disciplinas, professores)
        if dados is not None and botao not in ('cancelar', None):
            
            professor = self.pega_professor_pra_atividade()
            if(professor is None):
                self.__tela_atividade.showMessage(
                    'ERRO',
                    "ATENÇÃO: Professor não identificado, não foi possível adicionar atividade")
                return None
            disciplina = self.pega_disciplina_pra_atividade()
            if(disciplina is None):
                self.__tela_atividade.showMessage(
                    "ATENÇÃO: Disciplina não identificada, não foi possível adicionar atividade")
                return None

        self.__atividades.append(
            Atividade(dados["titulo"], dados["descricao"], dados["prazo"], professor, [], disciplina))

    def listar_atividades(self):
        if len(self.__atividades) == 0:
            self.__tela_atividade.showMessage("Nenhuma Atividade cadastrada")
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

    def inclui_atividade_aluno(self):
        self.listar_atividades()
        if len(self.__atividades) == 0:
            return None
        titulo = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo)

        aluno = self.pega_aluno_pra_atividade_aluno()
        if aluno is None:
            self.__tela_atividade.showMessage("ATENÇÃO: Aluno Inexistente.")
            return None
        if aluno not in atividade.disciplina.alunos:
            self.__tela_atividade.showMessage(
                "ATENÇÃO: Aluno não matriuclado nesta disciplina ")
            return None
        for atividade_aluno in atividade.atividades_aluno:
            if aluno == atividade_aluno.aluno:
                self.__tela_atividade.showMessage(
                    "ATENÇÃO: Aluno já possui esta atividade")
                return None

        dados = self.__tela_atividade.pega_dados_atividade_aluno()
        if dados is None:
            return None

        atividade.atividades_aluno.append(
            AtividadeAluno(dados["data_que_foi_entregue"], None, aluno, "ABERTA"))

    def entrega_atividade_aluno(self):
        self.listar_atividades()
        if len(self.__atividades) == 0:
            return None
        titulo = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo)
        aluno = self.pega_aluno_pra_atividade_aluno()
        if aluno is None:
            self.__tela_atividade.showMessage("ATENÇÃO: Aluno Inexistente.")
            return None
        for atividade_aluno in atividade.atividades_aluno:
            if aluno == atividade_aluno.aluno:
                atividade_aluno.status = "ENTREGUE"

    def avalia_atividade_aluno(self):
        self.listar_atividades()
        if len(self.__atividades) == 0:
            return None
        titulo = self.__tela_atividade.seleciona_atividade()
        atividade = self.pega_atividade_por_titulo(titulo)
        aluno = self.pega_aluno_pra_atividade_aluno()
        if aluno is None:
            self.__tela_atividade.showMessage("ATENÇÃO: Aluno Inexistente.")
            return None
        dados = self.__tela_atividade.pega_nota_atividade_aluno()
        if(dados is None):
            return None
        for atividade_aluno in atividade.atividades_aluno:
            if aluno == atividade_aluno.aluno:
                atividade_aluno.status = "AVALIADA"
                atividade_aluno.nota = dados["nota"]

    def pega_professor_pra_atividade(self):
        id = self.__controlador_sistema.controlador_professor.tela_professor.seleciona_professor()
        return self.__controlador_sistema.controlador_professor.pega_professor_por_id(id)

    def pega_aluno_pra_atividade_aluno(self):
        matricula = self.__controlador_sistema.controlador_aluno.tela_aluno.seleciona_aluno()
        return self.__controlador_sistema.controlador_aluno.pega_aluno_por_matricula(matricula)

    def pega_disciplina_pra_atividade(self):
        nome = self.__controlador_sistema.controlador_disciplina.tela_disciplina.seleciona_disciplina()
        return self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_nome(nome)
