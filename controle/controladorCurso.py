

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
            lista_opcoes[self.__tela_curso.mostra_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def listar_cursos(self):
        if len(self.__cursos) == 0:
            self.__tela_curso.mostra_msg("Nenhum curso cadastrado")
        else:
            for curso in self.__cursos:
                print('Curso: ', curso.nome)
                for disciplina in curso.disciplinas:
                    print('Disciplinas:')
                    print(disciplina)
            print()

    def inclui_curso(self):
        if len(self.__controlador_sistema._ControladorSistema__controlador_disciplina.disciplinas) == 0:
            self.__tela_curso.mostra_msg('Primeiro cadastre uma disciplina.')
        else:
            dados = self.__tela_curso.pega_dados_curso()
            # Para cada disciplina pega do usuário, compara com as disciplinas existentes e dispara msg caso disciplina não exista.
            for disciplina in dados['disciplinas']:
                for disciplina_cadastrada in self.__controlador_sistema.controlador_disciplina.disciplinas:
                    if disciplina not in self.__controlador_sistema.controlador_disciplina.disciplinas[0].nome:
                        self.__tela_curso.mostra_msg(
                            'Disciplina ' + str(disciplina) + ' não existente.')
                    else:
                        self.__cursos.append(
                            Curso(dados['nome'], dados['disciplinas']))

    def altera_curso(self):
        self.listar_cursos()
        nome = self.__tela_curso.seleciona_curso()
        curso = self.pega_curso_por_nome(nome)

        if curso is not None:
            novos_dados = self.__tela_curso.pega_dados_curso()
            curso.nome = novos_dados["nome"]
            curso.disciplinas = novos_dados["disciplinas"]
            self.listar_cursos()
        else:
            self.__tela_curso.mostra_msg("ATENÇÃO: Curso inexistente")

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
