

from exceptions.inputException import InputException
from dao.disciplinaDAO import DisciplinaDAO
from entidades.professor import Professor
from entidades.disciplina import Disciplina
from limite.telaDisciplina import TelaDisciplina
from controle.abstractControlador import AbstractControlador


class ControladorDisciplina(AbstractControlador):

    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__disciplinas = []
        self.__tela_disciplina = TelaDisciplina()
        self.__disciplina_dao = DisciplinaDAO()

    @property
    def disciplinas(self) -> list:
        return self.__disciplinas

    def tem_disciplinas(self):
        return len(self.__disciplina_dao.getAll()) > 0

    @property
    def tela_disciplina(self) -> TelaDisciplina:
        return self.__tela_disciplina

    def pega_disciplina_por_nome(self, nome: str):
        for disciplina in self.__disciplinas:
            if disciplina.nome == nome:
                return disciplina

        return None

    def pega_disciplina_por_codigo(self, codigo: int):
        for disciplina in self.__disciplina_dao.getAll():
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
            botao, dados = self.tela_disciplina.mostra_opcoes()
            if botao is None:
                botao = 0
            lista_opcoes[botao]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def inclui_disciplina(self):
        try:
            if(self.__controlador_sistema.controlador_professor.professores_len() == 0):
                self.__tela_disciplina.showMessage(
                    "ERRO",
                    "ATENÇÃO: Cadastre um Professor para poder adicionar uma disciplina!")
                return

            # Cria dicionario com professores para mostrar na tela
            professores = []
            # TODO: VALIDAR DEPOIS COM PERSISTENCIA
            for professor in self.__controlador_sistema.controlador_professor.professores:
                professores.append(
                    {"codigo": professor.id, "nome": professor.nome})

            # Pega dados
            button, values = self.__tela_disciplina.pega_dados_disciplina(
                professores)

            if button == "Cancelar" or button is None:
                return

            self.validar_formulario(button, values)

            # Encontra o professor selecionado
            professor_disciplina = None
            for key in values:
                if key == "codigo" or key == "nome" or key == "limite_alunos":
                    continue
                if values[key]:
                    professor_disciplina = self.__controlador_sistema.controlador_professor.pega_professor_por_id(
                        key)
            if (professor_disciplina) == None:
                raise InputException(
                    'A Disciplina deve ter um Professor para ministrá-la')

            nova_disciplina = Disciplina(values["nome"], [
            ], professor_disciplina, values["limite_alunos"], values["codigo"])
            self.__disciplina_dao.add(nova_disciplina)

            # TODO: Usar ProfessorDAO aqui
            professor.disciplinas.append(nova_disciplina)
            self.__tela_disciplina.showMessage(
                "Sucesso!", "Disciplina cadastrada")
        except InputException as e:
            self.__tela_disciplina.showMessage(
                "ERRO NA VALIDAÇÃO DO FORMULÁRIO", str(e))
            self.inclui_disciplina()
        except Exception as e:
            print(e)
            self.__tela_disciplina.showMessage(
                "ERRO", "Ocorreu um erro durante o registro da Disciplina")

    def altera_disciplina(self):
        try:
            if len(self.getAllDisciplinas()) == 0:
                self.__tela_disciplina.showMessage(
                    "Erro", "Nenhuma disciplina cadastrada! \n")
                # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
                return -1
            button_selecionar, values_selecionar = self.__tela_disciplina.seleciona_disciplina(
                self.cria_dicionario_disciplinas())

            if button_selecionar == "Voltar":
                return

            # Pega a instancia da disciplina selecionado
            disciplina_selecionada = None
            for key in values_selecionar:
                if values_selecionar[key]:
                    disciplina_selecionada = self.pega_disciplina_por_codigo(
                        key)
            # Cria dicionario com professores para mostrar na tela
            professores = []
            # TODO: VALIDAR DEPOIS COM PERSISTENCIA
            for professor in self.__controlador_sistema.controlador_professor.professores:
                professores.append(
                    {"codigo": professor.id, "nome": professor.nome})

            # Pega dados
            button, values = self.__tela_disciplina.pega_dados_disciplina(
                professores)

            if button == "Cancelar" or button is None:
                return

            self.validar_formulario(button, values, isUpdate=True)

            # Encontra o professor selecionado
            professor_disciplina = None
            for key in values:
                if key == "codigo" or key == "nome" or key == "limite_alunos":
                    continue
                if values[key]:
                    professor_disciplina = self.__controlador_sistema.controlador_professor.pega_professor_por_id(
                        key)
            if (professor_disciplina) == None:
                raise InputException(
                    'A Disciplina deve ter um Professor para ministrá-la')

            # disciplina_selecionada.codigo = values["codigo"]
            disciplina_selecionada.nome = values["nome"]
            disciplina_selecionada.limite_alunos = values["limite_alunos"]
            disciplina_selecionada.professor = professor

            self.__disciplina_dao.update(disciplina_selecionada)
            self.__tela_disciplina.showMessage(
                "Sucesso!", "Disciplina alterada com sucesso")
        except InputException as e:
            self.__tela_disciplina.showMessage(
                "ERRO NA VALIDAÇÃO DO FORMULÁRIO", str(e))
            self.inclui_disciplina()
        except Exception as e:
            print(e)
            self.__tela_disciplina.showMessage(
                "ERRO", "Ocorreu um erro ao alterar a Disciplina")

    def exclui_disciplina(self):
        try:
            if len(self.getAllDisciplinas()) == 0:
                self.__tela_disciplina.showMessage(
                    "Erro", "Nenhuma disciplina cadastrada! \n")
                # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
                return -1
            button_selecionar, values_selecionar = self.__tela_disciplina.seleciona_disciplina(
                self.cria_dicionario_disciplinas())
            if button_selecionar == "Voltar":
                return
            # Remove a Disiplina selecionada
            for key in values_selecionar:
                if values_selecionar[key]:
                    self.__disciplina_dao.remove(int(key))
            self.__tela_disciplina.showMessage(
                "Sucesso!", "Disciplina excluida")
        except Exception as e:
            print(e)
            self.__tela_disciplina.showMessage(
                "ERRO", "Ocorreu um erro ao excluir a Disciplina")

    def listar_disciplinas(self):

        if len(self.getAllDisciplinas()) == 0:
            return self.__tela_disciplina.showMessage("ERRO", "Nenhuma disicplina Cadastrada")

        disciplinas = []
        for disciplina in self.getAllDisciplinas():
            alunos = []
            for aluno in disciplina.alunos:
                alunos.append(
                    {"codigo": str(aluno.matricula), "nome": aluno.nome})
            disciplinas.append({"nome": disciplina.nome, "codigo": disciplina.codigo,
                                "limite_alunos": disciplina.limite_alunos, "professor": {"codigo":  disciplina.professor.id, "nome":  disciplina.professor.nome}, "alunos": alunos})
        self.__tela_disciplina.mostra_disciplinas(disciplinas)

    def inclui_aluno(self):
        try:
            # Seleciona Disciplina
            if len(self.getAllDisciplinas()) == 0:
                self.__tela_disciplina.showMessage(
                    "Erro", "Nenhuma disciplina cadastrada! \n")
                # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
                return -1
            button_selecionar, values_selecionar = self.__tela_disciplina.seleciona_disciplina(
                self.cria_dicionario_disciplinas())

            if button_selecionar == "Voltar":
                return

            # Pega a instancia da disciplina selecionado
            disciplina_selecionada = None
            for key in values_selecionar:
                if values_selecionar[key]:
                    disciplina_selecionada = self.pega_disciplina_por_codigo(
                        key)

            if int(disciplina_selecionada.limite_alunos) == len(disciplina_selecionada.alunos):
                raise InputException(
                    "Esta disciplina já atingiu o Limite de Alunos")

            botao, novos_dados = self.__controlador_sistema.controlador_aluno.tela_aluno.seleciona_aluno_para_alterar()
            if botao in ('cancelar', None):
                return
            aluno = self.__controlador_sistema.controlador_aluno.pega_aluno_por_matricula(
                novos_dados['matricula'])

            if aluno is None:
                raise InputException(
                    "Nenhum aluno encontrado com esta matrícula")

            disciplina_selecionada.alunos.append(aluno)
            self.__disciplina_dao.update(disciplina_selecionada)

            # TODO: Validar inclusão do aluno em seu controlador
            aluno.disciplinas.append(disciplina_selecionada)

            self.__tela_disciplina.showMessage(
                "Sucesso!", "Aluno matriculado a disciplina " + disciplina_selecionada.nome)

        except InputException as e:
            self.__tela_disciplina.showMessage(
                "ERRO NA VALIDAÇÃO DO FORMULÁRIO", str(e))
            self.inclui_disciplina()
        except Exception as e:
            print(e)
            self.__tela_disciplina.showMessage(
                "ERRO", "Ocorreu um erro ao alterar a Disciplina")

    def exclui_aluno(self):
        try:
            # Seleciona Disciplina
            if len(self.getAllDisciplinas()) == 0:
                self.__tela_disciplina.showMessage(
                    "Erro", "Nenhuma disciplina cadastrada! \n")
                # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
                return -1
            button_selecionar, values_selecionar = self.__tela_disciplina.seleciona_disciplina(
                self.cria_dicionario_disciplinas())

            if button_selecionar == "Voltar":
                return

            # Pega a instancia da disciplina selecionado
            disciplina_selecionada = None
            for key in values_selecionar:
                if values_selecionar[key]:
                    disciplina_selecionada = self.pega_disciplina_por_codigo(
                        key)

            if int(disciplina_selecionada.limite_alunos) == len(disciplina_selecionada.alunos):
                raise InputException(
                    "Esta disciplina já atingiu o Limite de Alunos")

            botao, novos_dados = self.__controlador_sistema.controlador_aluno.tela_aluno.seleciona_aluno_para_alterar()
            if botao in ('cancelar', None):
                return
            aluno = self.__controlador_sistema.controlador_aluno.pega_aluno_por_matricula(
                novos_dados['matricula'])

            if aluno is None:
                raise InputException(
                    "Nenhum aluno encontrado com esta matrícula")

            disciplina_selecionada.alunos.remove(aluno)
            self.__disciplina_dao.update(disciplina_selecionada)

            # TODO: Validar inclusão do aluno em seu controlador
            aluno.disciplinas.remove(disciplina_selecionada)

            self.__tela_disciplina.showMessage(
                "Sucesso!", "Aluno matriculado a disciplina " + disciplina_selecionada.nome)

        except InputException as e:
            self.__tela_disciplina.showMessage(
                "ERRO NA VALIDAÇÃO DO FORMULÁRIO", str(e))
            self.inclui_disciplina()
        except Exception as e:
            print(e)
            self.__tela_disciplina.showMessage(
                "ERRO", "Ocorreu um erro ao alterar a Disciplina")

    def validar_formulario(self, button, values, isUpdate=False):
        disciplinas_existentes = []
        for disciplina in self.__disciplina_dao.getAll():
            disciplinas_existentes.append(disciplina.codigo)
        if not isUpdate and values['codigo'] in disciplinas_existentes:
            raise InputException("Já exsite uma disciplina com este código")
        if not isUpdate and values["codigo"] == "":
            raise InputException("O Campo Código é obrigatório ")
        if not values["codigo"].isnumeric():
            raise InputException("O Campo Código deve ser um número inteiro ")
        if values["limite_alunos"] == "":
            raise InputException("O Campo Limite de Alunos é obrigatório ")
        if values["nome"] == "":
            raise InputException("O Campo Nome é obrigatório ")

    def getAllDisciplinas(self):
        return self.__disciplina_dao.getAll()

    def cria_dicionario_disciplinas(self):
        lista = []
        for disciplina in self.getAllDisciplinas():
            lista.append({"codigo": disciplina.codigo,
                         "nome": disciplina.nome})
        return lista
