

from entidades import disciplina
from dao.atividadeDAO import AtividadeDAO
from entidades.atividadeAluno import AtividadeAluno
from entidades.atividade import Atividade
from limite.telaAtividade import TelaAtividade
from entidades.curso import Curso
from entidades.aluno import Aluno
from controle.abstractControlador import AbstractControlador
from datetime import datetime


class ControladorAtividade(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__atividades = []
        self.__tela_atividade = TelaAtividade()
        self.__atividade_dao = AtividadeDAO()

    @property
    def tela_atividade(self) -> TelaAtividade:
        return self.__tela_atividade

    @property
    def atividades(self) -> list:
        return self.__atividades

    def pega_atividade_por_codigo(self, codigo: int):
        for atividade in self.__atividade_dao.getAll():
            if atividade.codigo == codigo:
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
        try:
            disciplinas = []
            for disc in self.__controlador_sistema.controlador_disciplina.disciplina_dao.getAll():
                disciplinas.append({'nome': disc.nome, 'codigo': disc.codigo})

            professores = []
            for prof in self.__controlador_sistema.controlador_professor.professor_dao.getAll():
                professores.append({'nome': prof.nome, 'id': prof.id})

            botao, dados = self.__tela_atividade.seleciona_atividade_para_alterar()
            if dados is not None and botao not in ('cancelar', None):
            
                atividade = self.pega_atividade_por_codigo(int(dados['codigo']))

                if atividade is not None:
                    botao, novos_dados = self.__tela_atividade.pega_novos_dados_atividade()
                    if novos_dados is None:
                        return None
                    for key in novos_dados.keys():
                        if novos_dados[key] == '':
                            self.__tela_atividade.showMessage(
                                'ERRO',
                                "ATENÇÃO: É necessário preencher todos os campos!")
                            return None

                    codigo_repetido = False
                    for ativ in self.__atividade_dao.getAll():
                        if novos_dados['codigo'] == ativ.codigo and novos_dados['codigo'] != atividade.codigo:
                            codigo_repetido = True
                            self.__tela_atividade.showMessage(
                                'ERRO',
                                "ATENÇÃO: Este código já está sendo utilizado!")
                            return None
                    
                    if codigo_repetido == False:
                        id_position = dados['professor'].find('=')         
                        cod_position = dados['disciplina'].find('=')
                    
                        professor_id = dados['professor'][id_position + 1:]
                        disciplina_cod = dados['disciplina'][cod_position + 1:]

                        professor = self.__controlador_sistema.controlador_professor.pega_professor_por_id(int(professor_id))
                        disciplina = self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_codigo(disciplina_cod)
                        dados['prazo_entrega'] = datetime.strptime(
                            str(dados['prazo_entrega']), "%d/%m/%Y")

                        atividade_alterada = Atividade(
                            dados["titulo"],
                            dados["descricao"],
                            dados["prazo_entrega"],
                            professor,
                            atividade.atividades_aluno,
                            disciplina,
                            int(dados['codigo'])
                            )

                        self.__professor_dao.remove(atividade.codigo)
                        self.__atividade_dao.add(atividade_alterada)
                        self.__tela_atividade.showMessage(
                                'SUCESSO',
                                "Atividade alterada!")
                else:
                    self.__tela_atividade.showMessage(
                        'ERRO',
                        "ATENÇÃO: Atividade inexistente")
            else: 
                return None
        except ValueError:
            self.__tela_atividade.showMessage(
                'ERRO',
                "Um ou mais valores inseridos não estão corretos!")
        except Exception:
            self.__tela_atividade.showMessage(
                'ERRO',
                "Houve problema ao adicionar atividade!")

    def exclui_atividade(self):
        try:
            botao, dados = self.__tela_atividade.seleciona_atividade_para_excluir()
            if botao not in ('cancelar', None):
                atividade = self.pega_atividade_por_codigo(int(dados['codigo']))
                if atividade is not None:
                    self.__atividade_dao.remove(int(atividade.codigo))
                    self.__tela_atividade.showMessage(
                        'SUCESSO',
                        "Atividade excluída!")
                else:
                    self.__tela_atividade.showMessage(
                        'ERRO',
                        "ATENÇÃO: Atividade inexistente")
            else:
                return None
        except ValueError:
            self.__tela_atividade.showMessage(
                'ERRO',
                "Um ou mais valores inseridos não estão corretos!")
        except Exception:
            self.__tela_atividade.showMessage(
                'ERRO',
                "Houve problema ao excluir atividade!")

    def inclui_atividade(self):
        try:
            disciplinas = []
            for disc in self.__controlador_sistema.controlador_disciplina.disciplina_dao.getAll():
                disciplinas.append({'nome': disc.nome, 'codigo': disc.codigo})

            professores = []
            for prof in self.__controlador_sistema.controlador_professor.professor_dao.getAll():
                professores.append({'nome': prof.nome, 'id': prof.id})

            botao, dados = self.__tela_atividade.pega_dados_atividade(disciplinas, professores)
            
            if dados is not None and botao not in ('cancelar', None):
                
                for key in dados.keys():
                    if dados[key] == '':
                        self.__tela_atividade.showMessage(
                            'ERRO',
                            "ATENÇÃO: É necessário preencher todos os campos!")
                        return None

                codigo_repetido = False
                for atividade in self.__atividade_dao.getAll():
                    if dados['codigo'] == atividade.codigo:
                        codigo_repetido = True
                        self.__tela_atividade.showMessage(
                            'ERRO',
                            "ATENÇÃO: Este código já está sendo utilizado!")
                        return None

                if codigo_repetido == False:
                    id_position = dados['professor'].find('=')         
                    cod_position = dados['disciplina'].find('=')
                
                    professor_id = dados['professor'][id_position + 1:]
                    disciplina_cod = dados['disciplina'][cod_position + 1:]

                    professor = self.__controlador_sistema.controlador_professor.pega_professor_por_id(int(professor_id))
                    disciplina = self.__controlador_sistema.controlador_disciplina.pega_disciplina_por_codigo(disciplina_cod)
                    dados['prazo_entrega'] = datetime.strptime(
                        str(dados['prazo_entrega']), "%d/%m/%Y")

                    nova_atividade = Atividade(
                        dados["titulo"],
                        dados["descricao"],
                        dados["prazo_entrega"],
                        professor,
                        [],
                        disciplina,
                        int(dados['codigo'])
                        )

                    self.__atividade_dao.add(nova_atividade)
                    self.__tela_atividade.showMessage(
                            'SUCESSO',
                            "Atividade cadastrada!")
        except ValueError:
            self.__tela_atividade.showMessage(
                'ERRO',
                "Um ou mais valores inseridos não estão corretos!")
        except Exception:
            self.__tela_atividade.showMessage(
                'ERRO',
                "Houve problema ao adicionar atividade!")

    def listar_atividades(self):
        try:
            if len(self.__atividade_dao.getAll()) == 0:
                self.__tela_atividade.showMessage(
                    'ERRO',
                    "Nenhuma Atividade cadastrada")
            else:
                atividades = {}
                for atividade in self.__atividade_dao.getAll():
                    atividades_aluno = []

                    for entrega in atividade.atividades_aluno:
                        atividades_aluno.append(
                            {"nome": entrega.aluno.nome,
                            "data_que_foi_entregue": entrega.data_que_foi_entregue,
                            "nota": entrega.nota,
                            "status": entrega.status})

                    atividades[atividade.codigo] = {
                        'titulo': atividade.titulo,
                        'descricao': atividade.descricao,
                        'prazo_entrega': atividade.prazo,
                        'professor': atividade.professor_responsavel.nome,
                        'disciplina': atividade.disciplina.nome,
                        'atividades_aluno': atividades_aluno
                    }
                self.__tela_atividade.mostra_atividades(atividades)
        except Exception:
            self.__tela_atividade.showMessage(
                'ERRO',
                "Houve um problema ao listar atividades!")

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
