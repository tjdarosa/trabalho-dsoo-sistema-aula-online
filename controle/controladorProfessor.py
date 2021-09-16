

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
    def tela_professor(self) -> TelaProfessor:
        return self.__tela_professor

    def pega_professor_por_id(self, id: int) -> Professor:
        for professor in self.__professores:
            if professor.id == id:
                return professor
        return None

    def abre_tela(self):
        lista_opcoes = {0: self.retornar,
                        1: self.listar_professores, 2: self.inclui_professor, 3: self.altera_professor, 4: self.exclui_professor}
        while True:
            lista_opcoes[self.__tela_professor.mostra_opcoes()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def altera_professor(self):
        self.listar_professores()
        id = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_id(id)

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
                                self.__tela_professor.mostra_msg('Este id já está sendo utilizado!\n')
                                id_repetido = True
                                break

                    if id_repetido == False:
                        professor.nome = novos_dados["nome"]
                        professor.idade = novos_dados["idade"]
                        self.__tela_professor.mostra_msg('Professor alterado!\n')
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
                self.__tela_professor.mostra_msg('Professor excluído com sucesso!\n')
            self.listar_professores()
        else:
            self.__tela_professor.mostra_msg(
                "ATENÇÃO: Professor inexistente")

    def inclui_professor(self):
        dados = self.__tela_professor.pega_dados_professor()
        if dados is not None:
            if (not isinstance(dados['idade'], int)) or (dados["idade"] > 150 or dados["idade"] < 0):
                self.__tela_professor.mostra_msg(
                    "ATENÇÃO: Insira um valor numérico entre 0 e 150!\n")
            else:
                # verifica se o id já existe.
                id_repetido = False
                if len(self.__professores) > 0:
                    for professor in self.__professores:
                        if dados['id'] == professor.id:
                            self.__tela_professor.mostra_msg('Este id já está sendo utilizado!\n')
                            id_repetido = True
                            break
        
                if not id_repetido:
                    self.__professores.append(
                        Professor(dados["nome"], dados["idade"], [], dados["id"]))
                    self.__tela_professor.mostra_msg('Professor adicionado!\n')
        else:
            return None


    def listar_professores(self):
        if len(self.__professores) == 0:
            self.__tela_professor.mostra_msg("Nenhum professor cadastrado")
        else:
            for professor in self.__professores:
                disciplinas = []
                for disciplina in professor.disciplinas:
                    disciplinas.append({"nome": disciplina.nome})
                self.__tela_professor.mostra_professor(
                    {"nome": professor.nome, "idade": professor.idade, "disciplinas": disciplinas, "id": professor.id})

    def professores_len(self) -> int:
        return len(self.__professores)
