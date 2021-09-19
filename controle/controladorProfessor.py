

from entidades.professor import Professor
from entidades.disciplina import Disciplina
from limite.telaProfessor import TelaProfessor
from controle.abstractControlador import AbstractControlador


class ControladorProfessor(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__professores = []
        self.__tela_professor = TelaProfessor()

    @property
    def professores(self) -> list:
        return self.__professores

    @property
    def tela_professor(self) -> TelaProfessor:
        return self.__tela_professor

    def pega_professor_por_id(self, id: int) -> Professor:
        for professor in self.__professores:
            if professor.id == id:
                return professor
        return None

    def abre_tela(self):
        try:
            lista_opcoes = {0: self.retornar,
                            1: self.listar_professores,
                            2: self.inclui_professor,
                            3: self.altera_professor,
                            4: self.exclui_professor}
            while True:
                botao, dados = self.__tela_professor.open()
                self.__tela_professor.close()
                lista_opcoes[botao]()
        except KeyError:
            print(botao, dados)
            self.__tela_professor.init_components()
            self.abre_tela()

    def retornar(self):
        self.__tela_professor.close()
        self.__controlador_sistema.abre_tela()

    def altera_professor(self):
        botao, dados = self.__tela_professor.seleciona_professor()
        print(botao, dados)
        professor = self.pega_professor_por_id(dados)

        if professor is not None:
            novos_dados = self.__tela_professor.pega_dados_professor()

            if novos_dados is not None:
                if (not isinstance(novos_dados['idade'], int)) or (novos_dados["idade"] > 150 or novos_dados["idade"] < 0):
                    self.__tela_professor.mostra_msg(
                        "ATENÇÃO: Insira um valor numérico entre 0 e 150!\n")
                else:
                    # verifica se o id já existe.
                    id_repetido = False
                    if len(self.__professores) > 0:
                        for professor in self.__professores:
                            if novos_dados['id'] == professor.id:
                                self.__tela_professor.mostra_msg(
                                    'Este id já está sendo utilizado!\n')
                                id_repetido = True
                                break

                    if id_repetido == False:
                        professor.nome = novos_dados["nome"]
                        professor.idade = novos_dados["idade"]
                        self.__tela_professor.mostra_msg(
                            'Professor alterado!\n')
                        self.listar_professores()

            else:
                return None
        else:
            self.__tela_professor.mostra_msg(
                "ATENÇÃO: Professor inexistente")

    def exclui_professor(self):
        self.listar_professores()
        id = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_id(id)
        if professor is not None:
            ministrando_disciplina = False
            for disciplina in self.__controlador_sistema.controlador_disciplina.disciplinas:
                if disciplina.professor is professor:
                    self.__tela_professor.mostra_msg(
                        "ATENÇÃO: Este professor está ministrando uma disciplina. Não será possível excluí-lo\n")
                    ministrando_disciplina = True
                    return None
            if ministrando_disciplina == False:
                self.__professores.remove(professor)
                self.__tela_professor.mostra_msg(
                    'Professor excluído com sucesso!\n')
            self.listar_professores()
        else:
            self.__tela_professor.mostra_msg(
                "ATENÇÃO: Professor inexistente")

    def inclui_professor(self):
        try:
            botao, dados = self.__tela_professor.pega_dados_professor()
            if dados is not None and botao not in ('cancelar', None):
                # verifica se a idade está dentro do permitido
                if int(dados["idade"]) > 150 or int(dados["idade"]) < 0:
                    self.__tela_professor.showMessage(
                        'ERRO',
                        "ATENÇÃO: Insira um valor numérico entre 0 e 150!")
                else:
                    # verifica se o id já existe.
                    id_repetido = False
                    if len(self.__professores) > 0:
                        for professor in self.__professores:
                            if dados['id'] == professor.id:
                                self.__tela_professor.showMessage(
                                    'ERRO',
                                    'Este id já está sendo utilizado!')
                                id_repetido = True
                                break

                    if not id_repetido:
                        self.__professores.append(
                            Professor(dados["nome"], int(dados["idade"]), [], int(dados["id"])))
                        self.__tela_professor.showMessage(
                            'SUCESSO',
                            'Professor adicionado!')
            else:
                return None
        except ValueError:
            self.__tela_professor.showMessage(
                'ERRO',
                "Um ou mais valores inseridos não estão corretos!")
        except Exception:
            self.__tela_professor.showMessage(
                'ERRO',
                "Houve problema ao adicionar professor!")

    def listar_professores(self):
        if len(self.__professores) == 0:
            self.__tela_professor.showMessage(
                'ERRO',
                "Nenhum professor cadastrado!")
        else:
            professores = {}
            for professor in self.__professores:
                disciplinas = []
                for disciplina in professor.disciplinas:
                    disciplinas.append(disciplina.nome)
                professores[professor.nome] = {
                    'idade': professor.idade,
                    'id': professor.id,
                    'disciplinas': disciplinas}
            self.__tela_professor.mostra_professores(professores)

    def professores_len(self) -> int:
        return len(self.__professores)
