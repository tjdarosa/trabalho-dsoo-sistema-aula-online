

from entidades.curso import Curso
from limite.telaCurso import TelaCurso
from controle.abstractControlador import AbstractControlador
from controle.controladorDisciplina import ControladorDisciplina


class ControladorCurso(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__cursos = []
        self.__tela_curso = TelaCurso()

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
        if len(self.__cursos) == 0:
            self.__tela_curso.mostra_msg("Nenhum curso cadastrado! \n")
            # return -1 é utilizado para evitar geração de relatórios caso não exsitam cursos cadastrados.
            return -1
        else:
            for curso in self.__cursos:
                self.__tela_curso.mostra_curso(curso)

    def inclui_curso(self):
        try:
            if len(self.__controlador_sistema._ControladorSistema__controlador_disciplina.disciplinas) == 0:
                self.__tela_curso.showMessage("ERRO",
                                              'Primeiro cadastre uma disciplina.')
            else:
                # Cria uma lista com as disciplinas em dicionário
                disciplinas = []
                for disciplina in self.__controlador_sistema.controlador_disciplina.disciplinas:
                    disciplinas.append(
                        {"codigo": disciplina.codigo, "nome": disciplina.nome})

                # seleciona nome do curso e as disciplinas que ele terá.
                button, values = self.__tela_curso.pega_dados_curso(
                    disciplinas)

                # verifica se os dados não são vazios e se o nome do curso já existe.
                cursos_existentes = []
                for curso in self.__cursos:
                    cursos_existentes.append(curso.codigo)

                if values is None:
                    self.__tela_curso.showMessage("ERRO",
                                                  'Houve um erro na inserção de informações! \n')
                elif values['codigo'] in cursos_existentes:
                    self.__tela_curso.showMessage(
                        "ERRO", 'Curso já existente! \n')

                else:
                    # Encontra as disciplinas selecionadas
                    disciplinas_curso = []
                    for key in values:
                        if key == "codigo" or key == "nome":
                            continue
                        if values[key]:
                            disciplinas_curso.appen(
                                self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_codigo(key))

                    self.__cursos.append(
                        Curso(values['nome'], disciplinas_curso))
                    self.__tela_curso.mostra_msg('Curso cadastrado! \n')

        except Exception as e:
            print(e)
            self.__tela_curso.showMessage(
                "ERRO", "Ocorreu um erro durante o registro do Curso")

    def altera_curso(self):
        self.listar_cursos()
        nome = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_nome(nome)

        if curso is not None:
            # seleciona nome do curso e quantidade de disciplinas que ele terá.
            novos_dados = self.__tela_curso.pega_nome_qtd_disciplinas_curso()

            # verifica se os novos dados não são vazios e se o nome do curso já existe.
            cursos_existentes = []
            for curso in self.__cursos:
                cursos_existentes.append(curso.nome)
            if novos_dados is None:
                self.__tela_curso.mostra_msg(
                    'Houve um erro na inserção de informações! \n')
            elif novos_dados['nome'] in cursos_existentes:
                self.__tela_curso.mostra_msg('Curso já existente! \n')

            else:
                self.__controlador_sistema.controlador_disciplina.listar_disciplinas()
                disciplinas_curso = self.__tela_curso.pega_disciplinas_curso(
                    novos_dados['qtd_disciplinas'])

                # verifica se há disciplinas repetidas.
                if len(disciplinas_curso) != len(set(disciplinas_curso)):
                    self.__tela_curso.mostra_msg(
                        'Existem disciplinas repetidas! Tente novamente. \n')

                else:
                    # verifica se as disciplinas informadas existem.
                    disciplinas_existentes = []
                    disciplinas_validadas = []
                    for disciplina in self.__controlador_sistema.controlador_disciplina.disciplinas:
                        disciplinas_existentes.append(disciplina.nome)
                    for disciplina_recebida in disciplinas_curso:
                        if disciplina_recebida not in disciplinas_existentes:
                            self.__tela_curso.mostra_msg(
                                'Disciplina ' + '"' + str(disciplina_recebida) + '"' + ' informada não existe!')
                        elif disciplina_recebida in disciplinas_existentes:
                            disciplinas_validadas.append(disciplina_recebida)

                        if len(disciplinas_curso) == len(disciplinas_validadas):
                            curso.nome = novos_dados["nome"]
                            curso.disciplinas = disciplinas_curso
                            self.__tela_curso.mostra_msg('Curso alterado! \n')
        else:
            self.__tela_curso.mostra_msg("ATENÇÃO: Curso inexistente! \n")

    def exclui_curso(self):
        nome = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_nome(nome)
        if len(self.__cursos) > 0:
            for curso_cadastrado in self.__cursos:
                if curso_cadastrado.nome == curso.nome:
                    self.__cursos.remove(curso_cadastrado)
                    self.__tela_curso.mostra_msg(
                        'Curso excluído: ' + str(curso_cadastrado.nome))
                else:
                    self.__tela_curso.mostra_msg(
                        'Curso não encontrado. Não foi possível excluí-lo')
        else:
            self.__tela_curso.mostra_msg('Não há cursos cadastrados.')

    def pega_curso_por_nome(self, nome_curso: str) -> Curso:
        for curso in self.__cursos:
            if curso.nome == nome_curso:
                return curso

    @property
    def cursos(self):
        return self.__cursos
