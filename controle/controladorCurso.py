

from exceptions.codigoRepetidoException import CodigoRepetidoException
from dao.cursoDAO import CursoDAO
from PySimpleGUI.PySimpleGUI import Input
from exceptions.inputException import InputException
from entidades.curso import Curso
from limite.telaCurso import TelaCurso
from controle.abstractControlador import AbstractControlador
from controle.controladorDisciplina import ControladorDisciplina


class ControladorCurso(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        # self.__cursos = []
        self.__tela_curso = TelaCurso()
        self.__curso_dao = CursoDAO()

    def abre_tela(self):
        lista_opcoes = {0: self.retornar,
                        1: self.listar_cursos,
                        2: self.inclui_curso,
                        3: self.altera_curso,
                        4: self.exclui_curso}
        while True:
            button, _ = self.__tela_curso.mostra_opcoes()
            if button is None:
                button = 0
            lista_opcoes[button]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def listar_cursos(self):
        if len(self.__curso_dao.getAll()) == 0:
            self.__tela_curso.showMessage(
                "Erro", "Nenhum curso cadastrado! \n")
            # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
            return -1

        cursos_dicionario = self.cria_dicionario_cursos()

        self.__tela_curso.mostra_cursos(cursos_dicionario)

    def inclui_curso(self):
        try:
            if len(self.__controlador_sistema.controlador_disciplina.getAllDisciplinas()) == 0:
                self.__tela_curso.showMessage("ERRO",
                                              'Primeiro cadastre uma disciplina.')
                return

            # Cria uma lista com as disciplinas em dicionário
            disciplinas = []
            for disciplina in self.__controlador_sistema.controlador_disciplina.getAllDisciplinas():
                disciplinas.append(
                    {"codigo": disciplina.codigo, "nome": disciplina.nome})
            # seleciona nome do curso e as disciplinas que ele terá.
            button, values = self.__tela_curso.pega_dados_curso(
                disciplinas)

            if button == "Retornar" or button is None:
                return
            # verifica se os dados não são vazios e se o nome do curso já existe.
            self.validar_formulario(button, values)

            # Encontra as disciplinas selecionadas
            disciplinas_curso = []
            for key in values:
                if key == "codigo" or key == "nome":
                    continue
                if values[key]:
                    disciplinas_curso.append(
                        self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_codigo(key))
            if len(disciplinas_curso) == 0:
                raise InputException(
                    'Deve ser selecionado pelo menos uma Disciplina para o Curso')
            # Salva
            self.__curso_dao.add(
                Curso(values['nome'], disciplinas_curso, values["codigo"]))
            self.__tela_curso.showMessage(
                "Sucesso!", 'Curso cadastrado! \n')
        except CodigoRepetidoException as e:
            self.__tela_curso.showMessage(
                "ERRO NA INSERÇÃO", str(e))
            self.inclui_curso()
        except InputException as e:
            self.__tela_curso.showMessage(
                "ERRO NA VALIDAÇÃO DO FORMULÁRIO", str(e))
            self.inclui_curso()
        except Exception as e:
            print(e)
            self.__tela_curso.showMessage(
                "ERRO", "Ocorreu um erro durante o registro do Curso")

    def altera_curso(self):
        try:
            if len(self.__curso_dao.getAll()) == 0:
                self.__tela_curso.showMessage(
                    "Erro", "Nenhum curso cadastrado! \n")
                # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
                return -1
            button_selecionar, values_selecionar = self.__tela_curso.seleciona_curso(
                self.cria_dicionario_cursos())
            if button_selecionar == "Voltar":
                return

            # Pega a instancia do curso selecionado
            curso_selecionado = None
            for key in values_selecionar:
                if values_selecionar[key]:
                    curso_selecionado = self.pega_curso_por_codigo(key)

            # Cria uma lista com as disciplinas em dicionário
            disciplinas = []
            for disciplina in self.__controlador_sistema.controlador_disciplina.disciplinas:
                disciplinas.append(
                    {"codigo": disciplina.codigo, "nome": disciplina.nome})
            button, values = self.__tela_curso.pega_dados_curso(disciplinas)

            if button == "Retornar" or button is None:
                return
            self.validar_formulario(button, values)

            # Encontra as disciplinas selecionadas
            disciplinas_curso = []
            for key in values:
                if key == "codigo" or key == "nome":
                    continue
                if values[key]:
                    disciplinas_curso.append(
                        self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_codigo(key))
            if len(disciplinas_curso) == 0:
                raise InputException(
                    'Deve ser selecionado pelo menos uma Disciplina para o Curso')
            # Salva
            curso_selecionado.codigo = values["codigo"]
            curso_selecionado.nome = values["nome"]
            curso_selecionado.disciplinas = disciplinas_curso

            self.__curso_dao.update(curso_selecionado)

            self.__tela_curso.showMessage(
                "Sucesso!", 'Curso Alterado! \n')

        except InputException as e:
            self.__tela_curso.showMessage(
                "ERRO NA VALIDAÇÃO DO FORMULÁRIO", str(e))
            self.altera_curso()
        except Exception as e:
            self.__tela_curso.showMessage(
                "ERRO", "Ocorreu um erro durante a alteração do curso")

    def exclui_curso(self):
        try:
            if len(self.__curso_dao.getAll()) == 0:
                self.__tela_curso.showMessage(
                    "Erro", "Nenhum curso cadastrado! \n")
                # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
                return -1
            button_selecionar, values_selecionar = self.__tela_curso.seleciona_curso(
                self.cria_dicionario_cursos())
            if button_selecionar == "Voltar":
                return
            # Pega a instancia do curso selecionado
            curso_selecionado = None
            for key in values_selecionar:
                if values_selecionar[key]:
                    curso_selecionado = self.pega_curso_por_codigo(key)
            self.__curso_dao.remove(curso_selecionado.codigo)
            self.__tela_curso.showMessage(
                "Sucesso!", 'Curso Excluído! \n')
        except Exception as e:
            print(e)
            self.__tela_curso.showMessage(
                "ERRO", "Ocorreu um erro durante a exclusão do curso")

    def pega_curso_por_nome(self, nome_curso: str) -> Curso:
        for curso in self.__curso_dao.getAll():
            if curso.nome == nome_curso:
                return curso

    def pega_curso_por_codigo(self, codigo: str) -> Curso:
        for curso in self.__curso_dao.getAll():
            if curso.codigo == codigo:
                return curso

    def cria_dicionario_cursos(self):
        cursos_dicionario = []
        for curso in self.__curso_dao.getAll():
            curso_disciplinas = []
            for disciplina in curso.disciplinas:
                curso_disciplinas.append(
                    {"codigo": disciplina.codigo, "nome": disciplina.nome})
            cursos_dicionario.append(
                {"codigo": curso.codigo, "nome": curso.nome, "disciplinas": curso_disciplinas})

        return cursos_dicionario

    def validar_formulario(self, button, values):
        cursos_existentes = []
        for curso in self.__curso_dao.getAll():
            cursos_existentes.append(curso.codigo)
        if values['codigo'] in cursos_existentes:
            raise CodigoRepetidoException()
        if values["codigo"] == "":
            raise InputException("O Campo Código é Necessário ")
        if values["nome"] == "":
            raise InputException("O Campo Nome é Necessário ")
